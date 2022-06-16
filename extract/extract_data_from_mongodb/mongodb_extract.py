from datetime import timedelta
from botocore.exceptions import ClientError
from mongodb_model import MongoInstance
import configparser
import datetime
import boto3
import csv

# load the mongo_config values
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mongo_config", "hostname")
username = parser.get("mongo_config", "username")
password = parser.get("mongo_config", "password")
db_name = parser.get("mongo_config", "database")
collection_name = parser.get("mongo_config", "collection")

# load aws_config values
access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")

mongo = MongoInstance(username, password, hostname, db_name, collection_name)

start_date = datetime.datetime.today() - timedelta(days=1)
end_date = start_date + timedelta(days=1)

all_events = mongo.get_events(start_date, end_date)

export_file_events = "export_file_events.csv"

with open(export_file_events, "w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerows(all_events)


s3 = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key)
s3_file = export_file_events


def upload_file(filename, bucket_name, s3_file):
    try:
        s3.upload_file(filename, bucket_name, s3_file)
    except ClientError as e:
        print(str(e))
        return False
    return True


upload_file(
    filename=export_file_events, bucket_name=bucket_name, s3_file=export_file_events
)
