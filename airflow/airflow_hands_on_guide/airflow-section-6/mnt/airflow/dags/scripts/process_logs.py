import pandas as pd
from datetime import datetime

# Notice the name of the parameter is not important
# It could be named kwargs as well. I named it context just
# to show that this variable does exist since we use the parameter
# provide_context=True from the PythonOperator
def process_logs_func(**context):
    log_dir = context['templates_dict']['log_dir']
    filename = context['params']['filename']

    print("Log dir: {}".format(log_dir))
    print("Filename: {}".format(filename))
    logs = pd.read_csv(log_dir + "/" + filename, sep=";")
    logs.drop("index", axis=1, inplace=True)
    logs['timestamp'] = logs['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
    logs.rename(
            columns={
                'timestamp': 'processing_time',
                'ds_airflow': 'etl_execution_time'
                },
            inplace=True
            )
    logs.to_csv(log_dir + "/processed_log.csv", sep=";", index=False)