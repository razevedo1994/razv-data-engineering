#!/usr/bin/env bash

# Create the user airflow in the HDFS
hdfs dfs -mkdir -p    /user/airflow/
hdfs dfs -chmod g+w   /user/airflow

# Move to the AIRFLOW HOME directory
cd $AIRFLOW_HOME

# Export environement variables
export AIRFLOW__CORE__LOAD_EXAMPLES=False

# Initiliase the metadatabase
airflow db init

# Create User
airflow users create -e "admin@airflow.com" -f "airflow" -l "airflow" -p "airflow" -r "Admin" -u "airflow"

# Run the scheduler in background
airflow scheduler &> /dev/null &

# Run the web sever in foreground (for docker logs)
exec airflow webserver