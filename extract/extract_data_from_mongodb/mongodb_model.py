from pymongo import MongoClient


class MongoInstance:
    def __init__(self, username, password, hostname, db_name, collection_name):
        self.mongo_uri = f"mongodb+srv://{username}:{password}@{hostname}/{db_name}?retryWrites=true&w=majority"
        self.client = MongoClient(self.mongo_uri)
        self.mongodb = self.client[db_name]
        self.mongo_collection = self.mongodb[collection_name]

    def get_events(self, start_date, end_date):
        mongo_query = {
            "$and": [
                {"event_timestamp": {"$gte": start_date}},
                {"event_timestamp": {"$lt": end_date}},
            ]
        }

        event_docs = self.mongo_collection.find(mongo_query, batch_size=3000)

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

        return all_events
