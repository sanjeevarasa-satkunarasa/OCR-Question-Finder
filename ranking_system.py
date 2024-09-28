import pymongo
from difflib import SequenceMatcher

def get_most_similar_document_key(input_string, db_name, collection_name):
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]

    most_similar_key = None
    highest_similarity = 0

    # Iterate through all documents in the collection
    for document in collection.find():
        value = document.get("value", "")
        if isinstance(value, str):
            similarity = SequenceMatcher(None, input_string, value).ratio()
            if similarity > highest_similarity:
                highest_similarity = similarity
                most_similar_key = document.get("key")

    return most_similar_key

# Example usage
input_string = "Tegn grafene til ogf g i samme koordinatsystem, og bestem skjæringspunktet grafisk"
db_name = "admin"
collection_name = "results"
most_similar_key = get_most_similar_document_key(input_string, db_name, collection_name)
print(f"The key of the most similar document is: {most_similar_key}")
