import chromadb

client = chromadb.HttpClient()

try: 
    client.create_collection("files")

except:
    print("Collection already exists")
    
collection = client.get_collection("files")

# load all the github data

import os
for file in os.listdir('clean_data'):
    if file.endswith('.txt'):
        with open(f'clean_data/{file}', 'r') as f:
            text = f.read()
            collection.add(
                documents=[text],
                metadatas={"filename": file},
                ids=[file]
            )
            print(f'clean_data/{file} added to database')