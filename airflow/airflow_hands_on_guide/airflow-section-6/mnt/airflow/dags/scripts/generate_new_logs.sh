#!/bin/bash

# This script creates a log named filename  at DEST_PATH using macros, variables
# and templating from Airflow

# DEST_PATH corresponds to the destination path where the log file is going to be created
# Notice that DEST_PATH is created using templating, macros and variables with AIRFLOW
# var.value.source_path is a variable coming from the Airflow UI -> variables panel
# macros.ds_format() is a macro defined by Airflow
# ts_nodash is a variable defined by Airflow
# curly brackets allow to use Jinja Templating to replace placeholders with values at runtime
DEST_PATH={{ var.value.source_path }}/data/{{ macros.ds_format(ts_nodash, "%Y%m%dT%H%M%S", "%Y-%m-%d-%H-%M") }}

mkdir -p $DEST_PATH
echo "index;message;timestamp;ds_airflow" >> $DEST_PATH/{{ params.filename }}
echo "templated_log_dir not templated from params: {{ params.dir_ }}"
for i in {1..5}
do
    RANDOM_STRING=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
    CURRENT_TS=$(date +%s)
    # We template the variable ds in order to have the current executation date of the DAG
    # filename is given from the parameter params of the BashOperator
    echo "$i;$RANDOM_STRING;$CURRENT_TS;{{ ds }}" >> $DEST_PATH/{{ params.filename }}
done