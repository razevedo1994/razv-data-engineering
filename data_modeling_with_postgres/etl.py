import os
import numpy as np
import re
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    
    """
    Processes song files and uploads data to the tables artists and songs.
    Args:
        cur: The cursor from the database connection with psycopg2.
        filepath: The path to the directory that contains the files.
    Returns:
        None
    """
    
    # open song file
    df_song_file = pd.read_json(filepath, lines=True)
    
    # insert artist record
    artist_data = df_song_file[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values
    
    for record in artist_data:
        record_as_list = list(record)
        cur.execute(artist_table_insert, record_as_list)

    # insert song record
    song_data = df_song_file[['song_id', 'title', 'artist_id', 'year', 'duration']].values
    
    for song in song_data:
        song_as_list = list(song)
        cur.execute(song_table_insert, song_as_list)
    
def process_log_file(cur, filepath):
    
    """
     Processes log files and uploads data to the tables users and time.
        Args:
            cur: The cursor from the database connection with psycopg2.
            filepath: The path to the directory that contains the files. 
        Returns:
            None
    """
    
    # open log file
    df_log_file = pd.read_json(filepath, lines=True)
    
    # filter by NextSong action
    next_song_pages = df_log_file['page'] == 'NextSong'
    
    # convert timestamp column to datetime
    timestamp = df_log_file['ts']
    t = pd.to_datetime(timestamp)
    
    # insert time data records
    time_data = [t, t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year, t.dt.weekday]
    column_labels = ['timestamp', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    d = dict(zip(column_labels, time_data))
    time_df = pd.DataFrame(d)
    
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    df_log_file_clean = df_log_file[df_log_file['userId']!= '']
    user_df = df_log_file_clean[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df_log_file_clean.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None

        # insert songplay record
        ids = pd.Series([song_id, artist_id], index=['song_id', 'artist_id'])
        enriched_row = row.append(ids)
        songplay_data = enriched_row[['ts', 'userId', 'level', 'song_id', 'artist_id',
                                      'sessionId', 'location', 'userAgent']]
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    
    """
    Description: This function is responsible for listing the files in a directory,
    and then executing the ingest process for each file according to the function
    that performs the transformation to save it to the database.

    Arguments:
        cur: the cursor object.
        conn: connection to the database.
        filepath: log data or song data file path.
        func: function that transforms the data and inserts it into the database.

    Returns:
        None
    """
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()