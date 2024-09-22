def insert_mangodb(key,value):
    import pymongo
    
    # Connect to MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Select the database
    db = client["admin"]

    # Select the collection
    collection = db["results"]

    # Create a dictionary to insert
    document = {
    "key": key,
    "value": value
    }

    # Insert the document into the collection
    result = collection.insert_one(document)

    # Print the ID of the inserted document
    print("Document inserted with ID:", result.inserted_id)