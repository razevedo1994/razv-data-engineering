import configparser


# CONFIG
config = configparser.ConfigParser()
config.read("dwh.cfg")

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create = """CREATE TABLE IF NOT EXISTS staging_events (artist varchar,
                                                                            auth varchar,
                                                                            firstName varchar,
                                                                            gender varchar,
                                                                            itemInSession int,
                                                                            lastName varchar,
                                                                            length real,
                                                                            level varchar,
                                                                            location varchar,
                                                                            method varchar,
                                                                            page varchar,
                                                                            registration real,
                                                                            sessionId int,
                                                                            song varchar,
                                                                            status int,
                                                                            ts timestamp,
                                                                            userAgent varchar,
                                                                            userId int);
"""

staging_songs_table_create = """CREATE TABLE IF NOT EXISTS staging_songs (num_songs int,
                                                                        artist_id varchar,
                                                                        artist_latitude float,
                                                                        artist_longitude float,
                                                                        artist_location varchar,
                                                                        artist_name varhar,
                                                                        song_id varchar,
                                                                        title varchar,
                                                                        duration real,
                                                                        year int);
"""

songplay_table_create = """CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY,
                                                                start_time bigint NOT NULL,
                                                                user_id int NOT NULL REFERENCES users(user_id),
                                                                level varchar,
                                                                song_id varchar,
                                                                artist_id varchar REFERENCES artists(artist_id),
                                                                session_id int,
                                                                location text,
                                                                user_agent text);
"""

user_table_create = """CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY,
                                                        first_name varchar NOT NULL,
                                                        last_name varchar NOT NULL,
                                                        gender varchar NOT NULL,
                                                        level varchar);
"""

song_table_create = """CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY,
                                                        title varchar,
                                                        artist_id varchar REFERENCES artists(artist_id),
                                                        year int,
                                                        duration decimal);
"""

artist_table_create = """CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY,
                                                            name varchar,
                                                            location varchar,
                                                            latitude varchar,
                                                            longitude varchar);
"""

time_table_create = """CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY,
                                                        hour int,
                                                        day int,
                                                        week int,
                                                        month int,
                                                        year int,
                                                        weekday int);
"""

# STAGING TABLES

staging_events_copy = (
    """COPY staging_events from 's3://udacity-dend/log_data'
        credentials 'aws_iam_role={role_arn}'
        compupdate off statupdate off
        region 'us-west-2' format as JSON 's3://udacity-dend/log_json_path.json'
        timeformat as 'epochmillisecs';
"""
).format()

staging_songs_copy = (
    """
"""
).format()

# FINAL TABLES

songplay_table_insert = """
"""

user_table_insert = """
"""

song_table_insert = """
"""

artist_table_insert = """
"""

time_table_insert = """
"""

# QUERY LISTS

create_table_queries = [
    staging_events_table_create,
    staging_songs_table_create,
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    staging_events_table_drop,
    staging_songs_table_drop,
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [
    songplay_table_insert,
    user_table_insert,
    song_table_insert,
    artist_table_insert,
    time_table_insert,
]
