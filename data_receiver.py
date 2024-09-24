import json

# Read JSON data from the file
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the data
print(f"Input: {data['input']}")
