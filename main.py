import subprocess
import os
import pymongo
from mango_module import insert_mangodb

# Directory containing the PDF files
directory = '1T Files'

# Function to process PDF files
def process_pdfs(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.pdf'):
                # Full path to the PDF file
                pdf_path = os.path.join(root, filename)
                
                # Output file path
                output_file = os.path.join(root, f'{os.path.splitext(filename)[0]}_output.txt')
                
                # Call the cat command and redirect output
                with open(output_file, 'w') as output:
                    try:
                        subprocess.run(f'ocrmypdf --sidecar{filename}.txt {pdf_path} {output_file}')
                    # put some code to read the output file
                        content = file.read(f'{filename}.txt') 
                        insert_mangodb(f'{output_file}',content) # here x is 
                    except:
                        print('Error')

#the input pdf file name and y is the result of file reading of the output text file. 

# Start processing
process_pdfs(directory)

print("Processing complete.")

