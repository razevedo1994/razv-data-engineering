from pymongo import MongoClient
from datetime import timedelta
from botocore.exceptions import ClientError
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

mongo_uri = f"mongodb+srv://{username}:{password}@{hostname}/{db_name}?retryWrites=true&w=majority"

mongo_client = MongoClient(mongo_uri)

# connect to the db where the collection resides
mongo_db = mongo_client[db_name]

# choose the connection to query documents from
mongo_collection = mongo_db[collection_name]

start_date = datetime.datetime.today() - timedelta(days=1)
end_date = start_date + timedelta(days=1)

mongo_query = {
    "$and": [
        {"event_timestamp": {"$gte": start_date}},
        {"event_timestamp": {"$lt": end_date}},
    ]
}

event_docs = mongo_collection.find(mongo_query, batch_size=3000)  # cursor

# create a blank list to store the results
all_events = []

for doc in event_docs:
    event_id = str(doc.get("event_id", -1))
    event_timestamp = doc.get("event_timestamp", None)
    event_name = doc.get("event_name", None)

    current_event = []
    current_event.append(event_id)
    current_event.append(event_timestamp)
    current_event.append(event_name)

    all_events.append(current_event)

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
