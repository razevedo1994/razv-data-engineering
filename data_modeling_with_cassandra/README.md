### Project: Data Modeling with Cassandra

### Table of Contents

[Project Motivation](#Motivation)

[Project Overview](#ProjectOverview)

[Project Steps](#ProjectSteps)

[Build ETL Pipeline](#ETL)


### Project Motivation<a name="Motivation"></a>

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.


### Project Overview<a name="ProjectOverview"></a>

In this project, you'll apply what you've learned on data modeling with Apache Cassandra and complete an ETL pipeline using Python. To complete the project, you will need to model your data by creating tables in Apache Cassandra to run queries. You are provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.

We have provided you with a project template that takes care of all the imports and provides a structure for ETL pipeline you'd need to process this data.


### Project Steps<a name="ProjectSteps"></a>

- [x] Design tables to answer the queries outlined in the project template
- [x] Write Apache Cassandra CREATE KEYSPACE and SET KEYSPACE statements
- [x] Develop your CREATE statement for each of the tables to address each question
- [x] Load the data with INSERT statement for each of the tables
- [x] Include IF NOT EXISTS clauses in your CREATE statements to create tables only if the tables do not already exist. We recommend you also include DROP TABLE statement for each table, this way you can run drop and create tables whenever you want to reset your database and test your ETL pipeline
- [x] Test by running the proper select statements with the correct WHERE clause


### Build ETL Pipeline<a name="ETL"></a>

- [x] Implement the logic in section Part I of the notebook template to iterate through each event file in event_data to process and create a new CSV file in Python
- [x] Make necessary edits to Part II of the notebook template to include Apache Cassandra CREATE and INSERT statements to load processed records into relevant tables in your data model
- [x] Test by running SELECT statements after running the queries on your database
