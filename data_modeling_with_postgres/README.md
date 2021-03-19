### Project: Data Modeling with Postgres

### Table of Contents

[Project Motivation](#Motivation)

[Project Descriptions](#Description)

[Files Descriptions](#FilesDescriptions)

[Dimension Tables](#DimensionTables)

[How to run](#HowToRun)

### Project Motivation<a name="Motivation"></a>

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

### Project Descriptions<a name="Description"></a>

In this project, we will apply data modeling with Postgres and build an ETL pipeline using Python. To complete the project, we will define fact and dimension tables for a star schema for a particular analytical focus, and write an ETL pipeline that transfers data from files in two local directories to these tables in Postgres using Python and SQL.

### Files Descriptions<a name="FilesDescriptions"></a>

- test.ipynb displays the first few rows of each table to let you check your database.
- create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
- etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for - each of the tables.
- etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
- sql_queries.py contains all your sql queries, and is imported into the last three files above.


#### Dimension Tables<a name="DimensionTables"></a>

The following diagram shows all four dimension tables. These four tables will exist in postgres,
the code in this repository will upload the data to postgres.

<p align="center">
  <img src="diagram.png" >
</p>

In the center of the dimension table will be the fact table. together, these form
a star schema.



### How to run the python scripts<a name="HowToRun"></a>

Make sure that the machine that runs the scripts have Postgres installed and available.
Remember to run create_tables.py before running etl.py to restart your tables. Run test.ipynb to confirm that your records have been successfully inserted into each table.