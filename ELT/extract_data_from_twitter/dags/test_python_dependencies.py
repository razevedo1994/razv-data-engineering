from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {"owner": "azevedo", "retry": 5, "retry_delay": timedelta(minutes=5)}


def get_spark():
    import pyspark

    print(f"Version of pyspark is: {pyspark.__version__}")


with DAG(
    default_args=default_args,
    dag_id="test_python_dependencies",
    start_date=datetime(2022, 5, 7),
    schedule_interval="@daily",
) as dag:

    get_spark = PythonOperator(task_id="get_pyspark_version", python_callable=get_spark)

    get_spark
