import pymongo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_documents(input_string):
    # Connect to MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Select the database and collection
    db = client["mydatabase"]
    collection = db["mycollection"]
    
    # Fetch all documents from the collection
    documents = list(collection.find())
    
    # Extract the content from the documents
    contents = [doc.get("content", "") for doc in documents]
    
    # Add the input string to the contents list
    contents.append(input_string)
    
    # Compute TF-IDF vectors for the contents
    vectorizer = TfidfVectorizer().fit_transform(contents)
    
    # Compute cosine similarity between the input string and all documents
    cosine_similarities = cosine_similarity(vectorizer[-1], vectorizer[:-1]).flatten()
    
    # Create a list to store the ranking results
    ranking = [(doc, score) for doc, score in zip(documents, cosine_similarities)]
    
    # Sort the ranking list based on similarity score in descending order
    ranking.sort(key=lambda x: x[1], reverse=True)
    
    # Print the ranked documents
    for rank, (doc, score) in enumerate(ranking, start=1):
        print(f"Rank {rank}: {doc} with score {score}")
    
    # Close the MongoDB connection
    client.close()

# Example usage
input_string = "example"
rank_documents(input_string)
