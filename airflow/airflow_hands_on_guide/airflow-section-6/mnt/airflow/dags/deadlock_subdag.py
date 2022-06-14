import airflow
from subdags.subdag import factory_subdag
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator
from airflow.executors.celery_executor import CeleryExecutor

DAG_NAME="deadlock_subdag"

default_args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

with DAG(dag_id=DAG_NAME, default_args=default_args, schedule_interval="@once") as dag:
    start = DummyOperator(
        task_id='start'
    )

    subdag_1 = SubDagOperator(
        task_id='subdag-1',
        subdag=factory_subdag(DAG_NAME, 'subdag-1', default_args),
        executor=CeleryExecutor()
    )

    subdag_2 = SubDagOperator(
        task_id='subdag-2',
        subdag=factory_subdag(DAG_NAME, 'subdag-2', default_args),
        executor=CeleryExecutor()
    )

    subdag_3 = SubDagOperator(
        task_id='subdag-3',
        subdag=factory_subdag(DAG_NAME, 'subdag-3', default_args),
        executor=CeleryExecutor()
    )

    subdag_4 = SubDagOperator(
        task_id='subdag-4',
        subdag=factory_subdag(DAG_NAME, 'subdag-4', default_args),
        executor=CeleryExecutor()
    )

    final = DummyOperator(
        task_id='final'
    )

    start >> [subdag_1, subdag_2, subdag_3, subdag_4] >> final