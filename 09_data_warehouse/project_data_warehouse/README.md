# Project: Data Warehouse

### Introduction/Problem

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

### Objective

In this project, I build an ETL pipeline for a database hosted on Redshift. To complete the project, we will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

### Schema for Song Play Analysis
Using the song and event datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

##### Fact Table
**songplays**: Records in event data associated with song plays i.e. records with page NextSong
 - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

##### Dimension Tables
**users**: Users in the app
 - user_id, first_name, last_name, gender, level

**songs**: Songs in music database
 - song_id, title, artist_id, year, duration

**artists**: Artists in music database
 - artist_id, name, location, lattitude, longitude

**time**: Timestamps of records in songplays broken down into specific units
 - start_time, hour, day, week, month, year, weekday

### Project template

 - `launch_cluster.py`: Create a new IAM role and a redshift cluster.
 - `create_tables.py`: Is where you'll create your fact and dimension tables for the star schema in Redshift.
 - `etl.py`: Is where you'll load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.
 - `sql_queries.py`: Is where you'll define you SQL statements, which will be imported into the two other files above.

##### Execution order
`launch_cluster.py` > `create_table.py` > `etl.py`

### Used libraries

 - configparser
 - psycopg2
 - boto3
 - json
