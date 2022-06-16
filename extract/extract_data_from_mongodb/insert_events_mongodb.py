from pymongo import MongoClient
import datetime
import urllib
import configparser

# load the mongo_config values
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mongo_config", "hostname")
username = parser.get("mongo_config", "username")
password = parser.get("mongo_config", "password")
db_name = parser.get("mongo_config", "database")
collection_name = parser.get("mongo_config", "collection")

mongo_uri = (
    "mongodb+srv://"
    + username
    + ":"
    + password
    + "@"
    + hostname
    + "/"
    + db_name
    + "?retryWrites=true&w=majority"
)

mongo_client = MongoClient(mongo_uri)

# connect to the db where the collection resides
mongo_db = mongo_client[db_name]

# choose the connection to query documents from
mongo_collection = mongo_db[collection_name]

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
mongo_collection.insert_one(event_1)
mongo_collection.insert_one(event_2)
mongo_collection.insert_one(event_3)
mongo_collection.insert_one(event_4)
