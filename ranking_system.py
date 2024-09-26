import pymongo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_documents(input_string):
    """
    Rank documents in a MongoDB collection based on their similarity to an input string.

    Parameters:
    input_string (str): The input string to compare against the documents.

    Returns:
    str: The value of the 'key' field of the document with the highest similarity score.
    """
    try:
        # Connect to MongoDB server
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        
        # Select the database and collection
        db = client["admin"]
        collection = db["results"]
        
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
        
        # Find the document with the highest similarity score
        best_match_index = cosine_similarities.argmax()
        best_match_doc = documents[best_match_index]
        
        return best_match_doc.get("key", None)
    
    except pymongo.errors.PyMongoError as e:
        print(f"An error occurred: {e}")
        return None
    
    finally:
        # Close the MongoDB connection
        client.close()

# Example usage
input_string = "example"
best_doc_key = rank_documents(input_string)
print(f"The key of the best matching document is: {best_doc_key}")
