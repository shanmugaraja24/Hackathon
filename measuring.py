from pymongo import MongoClient

def calculate_compression_ratio():
    # Use a valid connection string for MongoDB
    client = MongoClient("mongodb://localhost:27017/")  # Example: Replace with your MongoDB URI
    db = client.test_db  
    collection = db.test_collection

    # Fetch documents from MongoDB (ensure your documents have the "type" field)
    json_doc = collection.find_one({"type": "json"})
    msgpack_doc = collection.find_one({"type": "msgpack"})

    # Calculate sizes
    json_size = len(json_doc["data"].encode("utf-8"))
    msgpack_size = len(msgpack_doc["data"])

    # Compression ratio
    compression_ratio = json_size / msgpack_size if msgpack_size != 0 else float('inf')

    return json_size, msgpack_size, compression_ratio
