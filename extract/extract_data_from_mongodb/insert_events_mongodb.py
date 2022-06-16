from pymongo import MongoClient
from mongodb_model import MongoInstance
import datetime
import configparser

# load the mongo_config values
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mongo_config", "hostname")
username = parser.get("mongo_config", "username")
password = parser.get("mongo_config", "password")
db_name = parser.get("mongo_config", "database")
collection_name = parser.get("mongo_config", "collection")

mongo = MongoInstance(username, password, hostname, db_name, collection_name)

event_1 = {
    "event_id": 1,
    "event_timestamp": datetime.datetime.today(),
    "event_name": "singup",
}

event_2 = {
    "event_id": 2,
    "event_timestamp": datetime.datetime.today(),
    "event_name": "pageview",
}

event_3 = {
    "event_id": 3,
    "event_timestamp": datetime.datetime.today(),
    "event_name": "login",
}

event_4 = {
    "event_id": 4,
    "event_timestamp": datetime.datetime.today(),
    "event_name": "order",
}

# insert events
events = [event_1, event_2, event_3, event_4]

for event in events:
    mongo.insert_event(event)
