import subprocess
import pymongo

# Running a shell command and capturing its output
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)

import os
import subprocess

# Directory containing the PDF files
directory = '/path/to/your/pdf/files'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        # Full path to the PDF file
        pdf_path = os.path.join(directory, filename)
        
        # Output file path
        output_file = os.path.join(directory, f'{os.path.splitext(filename)[0]}_output.txt')
        
        # Call the cat command and redirect output
        with open(output_file, 'w') as output:
            subprocess.run(['cat', pdf_path], stdout=output)
            # put some code to read the output file 
            insert_mangodb(x,y) # here x is the input pdf file name and y is the result of file reading of the output text file. 


print("Processing complete.")

#############################################################

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
