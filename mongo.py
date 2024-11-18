from pymongo import MongoClient

def store_in_mongo(json_data, msgpack_data):
    # Example MongoDB connection
    client = MongoClient("mongodb://localhost:27017/")  # Replace with actual MongoDB URI
    db = client.test_db
    collection = db.test_collection

    # Insert documents (ensure you have a schema)
    collection.insert_one({"type": "json", "data": json_data})
    collection.insert_one({"type": "msgpack", "data": msgpack_data})
