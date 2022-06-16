from datetime import timedelta
from mongodb_model import MongoInstance
from writer import write_file_local, write_file_on_s3
import configparser
import datetime


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

write_file_local(all_events, export_file_events)

write_file_on_s3(access_key, secret_key, export_file_events, bucket_name)
