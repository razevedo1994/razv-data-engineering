import configparser


# CONFIG
config = configparser.ConfigParser()
config.read_file(open("dwh.cfg"))
ARN = config.get('IAM_ROLE', 'ARN')

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
                                                                        artist_name varchar,
                                                                        song_id varchar,
                                                                        title varchar,
                                                                        duration real,
                                                                        year int);
"""

user_table_create = """CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY,
                                                        first_name varchar NOT NULL,
                                                        last_name varchar NOT NULL,
                                                        gender varchar NOT NULL,
                                                        level varchar);
"""

songplay_table_create = """CREATE TABLE IF NOT EXISTS songplays (songplay_id int PRIMARY KEY,
                                                                start_time bigint NOT NULL,
                                                                user_id int NOT NULL REFERENCES users(user_id),
                                                                level varchar,
                                                                song_id varchar,
                                                                artist_id varchar REFERENCES artists(artist_id),
                                                                session_id int,
                                                                location text,
                                                                user_agent text);
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
        credentials 'aws_iam_role=ARN'
        compupdate off statupdate off
        region 'us-west-2' format as JSON 's3://udacity-dend/log_json_path.json'
        timeformat as 'epochmillisecs';
"""
).format()

staging_songs_copy = (
    """COPY staging_songs from 's3://udacity-dend/song_data'
	    credentials 'aws_iam_role=ARN'
	    compupdate off statupdate off
	    region 'us-west-2' format as JSON 'auto';
"""
).format()

# FINAL TABLES

songplay_table_insert = """INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            SELECT se.ts as start_time,
                                    se.userId as user_id,
                                    se.level,
                                    ss.song_id,
                                    ss.artist_id,
                                    se.sessionId as session_id,
                                    se.location,
                                    se.userAgent as user_agent
                            FROM staging_events se, staging_songs ss
                            WHERE se.page = 'NextSong'
                            AND se.song = ss.title
                            AND se.userId NOT IN (SELECT DISTINCT sp.user.id,
                                                    FROM songplays as sp
                                                    WHERE sp.user_id IS NOT NULL
                                                    AND sp.user_id = se.userId
                                                    AND sp.session_id = se.sessionId
                                                    AND sp.user_id IN (SELECT user_id 
                                                                        FROM users));

"""

user_table_insert = """INSERT INTO users (user_id, first_name, last_name, gender, level)
                        SELECT DISTINCT se.userId as user_id,
                                        se.firstName as first_name,
                                        se.lastName as last_name,
                                        se.gender,
                                        se.level
                        FROM (SELECT userId,
                                    firstName,
                                    lastName,
                                    gender,
                                    level
                                FROM staging_events
                                WHERE userId IS NOT NULL
                                AND page = 'NextSong') se;
"""

song_table_insert = """INSERT INTO songs (song_id, title, artist_id, year, duration)
                        SELECT DISTINCT ss.song_id,
                                        ss.title,
                                        ss.artist_id,
                                        ss.year,
                                        ss.duration
                        FROM (SELECT song_id,
                                    title,
                                    artist_id,
                                    year,
                                    duration
                                FROM staging_songs
                                WHERE song_id IS NOT NULL) ss;
"""

artist_table_insert = """INSERT INTO artists (artist_id, name, location, latitude, longitude)
                            SELECT DISTINCT ss.artist_id,
                                            ss.artist_name as name,
                                            ss.artist_location as location,
                                            ss.artist_latitude as latitude,
                                            ss.artist_longitude as longitude
                            FROM (SELECT artist_id,
                                        artist_name,
                                        artist_location,
                                        artist_latitude,
                                        artist_longitude
                                    FROM staging_songs
                                    WHERE artist_id IS NOT NULL) ss;
"""

time_table_insert = """INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                        SELECT se.ts as start_time,
                                EXTRACT (hour FROM se.ts) as hour,
                                EXTRACT (day FROM se.ts) as day,
                                EXTRACT (week FROM se.ts) as week,
                                EXTRACT (month FROM se.ts) as month,
                                EXTRACT (year FROM se.ts) as year,
                                EXTRACT (weekday FROM se.ts) as weekday
                        FROM (SELECT DISTINCT ts
                                FROM staging_events) se;
"""

# QUERY LISTS

create_table_queries = [
    staging_events_table_create,
    staging_songs_table_create,
    user_table_create,
    artist_table_create,
    songplay_table_create,
    song_table_create,
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
