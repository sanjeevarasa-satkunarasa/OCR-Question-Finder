import pymongo

def rank_documents(input_string):
    # Connect to MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Select the database and collection
    db = client["mydatabase"]
    collection = db["mycollection"]
    
    # Fetch all documents from the collection
    documents = collection.find()
    
    # Create a list to store the ranking results
    ranking = []
    
    # Compare input string with each document's content field
    for doc in documents:
        content = doc.get("content", "")
        match_score = sum(1 for a, b in zip(input_string, content) if a == b)
        ranking.append((doc, match_score))
    
    # Sort the ranking list based on match_score in descending order
    ranking.sort(key=lambda x: x[1], reverse=True)
    
    # Print the ranked documents
    for rank, (doc, score) in enumerate(ranking, start=1):
        print(f"Rank {rank}: {doc} with score {score}")

# Example usage
input_string = "example"
rank_documents(input_string)
