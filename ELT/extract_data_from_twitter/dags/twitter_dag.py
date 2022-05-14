from datetime import datetime
from airflow.models import DAG
from os.path import join
from twitter_operator import main
from airflow.operators.python import PythonOperator

file_path = join(
            "home/razevedo/Projects/data-engineering/ELT/extract_data_from_twitter",
            "twitter_aluraonline",
            "extract_date={{ ds }}",
            "AluraOnline_{{ ds_nodash }}.json",
        )

with DAG(dag_id="twitter_dag", start_date=datetime.now()) as dag:
    twitter_operator = PythonOperator(
        task_id="extract_data_from_twitter",
        python_callable=main,
        op_kwargs={"query": "AluraOnline",
                   "file_path": file_path}
    )
