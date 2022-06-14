import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    "start_date": airflow.utils.dates.days_ago(1), 
    "owner": "Airflow"
}

def remote_value(**context):
    print("Value {} for key=message received from the controller DAG".format(context["dag_run"].conf["message"]))

with DAG(dag_id="triggerdagop_target_dag", default_args=default_args, schedule_interval=None) as dag:

    t1 = PythonOperator(
            task_id="t1",
            provide_context=True,
            python_callable=remote_value, 
        )

    t2 = BashOperator(
        task_id="t2",
        bash_command='echo Message: {{ dag_run.conf["message"] if dag_run else "" }}')

    t3 = BashOperator(
        task_id="t3",
        bash_command="sleep 30"
    )