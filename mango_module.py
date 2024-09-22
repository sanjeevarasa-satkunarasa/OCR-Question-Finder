def insert_mangodb(key,value):
    # Connect to MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Select the database
    db = client["mydatabase"]

    # Select the collection
    collection = db["mycollection"]

    # Create a dictionary to insert
    document = {
    "key": key,
    "value": value
    }

    # Insert the document into the collection
    result = collection.insert_one(document)

    # Print the ID of the inserted document
    print("Document inserted with ID:", result.inserted_id)