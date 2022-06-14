import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    }

with DAG(dag_id="logger_dag", default_args=default_args, schedule_interval="@daily") as dag:

    t1 = DummyOperator(task_id="t1")

    t2 = BashOperator(
            task_id="t2",
            bash_command="echo 'It works'"
        )

    t1 >> t2