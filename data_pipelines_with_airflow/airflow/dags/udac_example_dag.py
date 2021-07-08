from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries
import datetime
from airflow import conf
from airflow.operators.postgres_operator import PostgresOperator



AWS_KEY = os.environ.get('AWS_KEY')
AWS_SECRET = os.environ.get('AWS_SECRET')

default_args = {
    'owner': 'udacity',
    'depends_on_past': False,
    'start_date': datetime.datetime.now(),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    'schedule_interval': '@hourly',
}

dag = DAG('udac_example_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          start_date = datetime.datetime.now()
        )

dq_checks = [
    {'check_sql': "SELECT COUNT(*) FROM users WHERE userid is null",
     'expected_result': 0,
     'descr': "null values in users.userid column"},
    {'check_sql': "SELECT COUNT(*) FROM songs WHERE songid is null",
     'expected_result': 0,
     'descr': "null values in songs.songid column"},
    {'check_sql': "SELECT COUNT(*) FROM(SELECT cnt, count(*) FROM (SELECT "
        "songid, count(*) cnt FROM songs GROUP BY songid) GROUP BY cnt)",
     'expected_result': 1,
     'descr': "duplicate song ids found"},
    {'dual_sql1': "SELECT COUNT(*) songs_cnt FROM songs",
     'dual_sql2': "SELECT COUNT(DISTINCT song_id) st_sng_song_cnt "
        "FROM staging_songs",
     'descr': "# records in songs table and # DISTINCT staging_songs records"}
]

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

create_tables_task = PostgresOperator(
    task_id='create_tables',
    dag=dag,
    postgres_conn_id='redshift',
    sql='create_tables.sql'
)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Stage_events',
    dag=dag,    
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",    
    table = "staging_events",
    s3_path = "s3://udacity-dend/log_data",
    json_path="s3://udacity-dend/log_json_path.json"
)


stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='Stage_songs',
    dag=dag,  
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",    
    table = "staging_songs",
    s3_path = "s3://udacity-dend/song_data",
    json_path="auto"
)


load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    dag=dag,    
    redshift_conn_id="redshift",
    table="songplays",
    sql=SqlQueries.songplay_table_insert,
    append_only=False
)

load_songs_table = LoadDimensionOperator(
    task_id='Load_songs_table',
    dag=dag,   
    redshift_conn_id="redshift",
    table="songs",
    sql=SqlQueries.song_table_insert,
    append_only=False
)


load_users_table = LoadDimensionOperator(
    task_id='Load_users_table',
    dag=dag,   
    redshift_conn_id="redshift",
    table="users",
    sql=SqlQueries.user_table_insert,
    append_only=False
)

load_artists_table = LoadDimensionOperator(
    task_id='Load_artists_table',
    dag=dag,   
    redshift_conn_id="redshift",
    table="artists",
    sql=SqlQueries.artist_table_insert,
    append_only=False
)

load_time_table = LoadDimensionOperator(
    task_id='Load_time_table',
    dag=dag,   
    redshift_conn_id="redshift",
    table="time",
    sql=SqlQueries.time_table_insert,
    append_only=False
)


run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    provide_context=True,
    redshift_conn_id="redshift",
    checks=dq_checks
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)


create_tables_task
start_operator >> [stage_events_to_redshift, stage_songs_to_redshift] \
    >> load_songplays_table \
    >> [ load_songs_table, load_artists_table, load_time_table, load_users_table] \
    >> run_quality_checks \
    >> end_operator
