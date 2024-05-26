from fastapi import FastAPI,File, UploadFile, Query
import chromadb
app = FastAPI(docs_url="/")

client = chromadb.HttpClient()
collection = client.get_collection("files")


@app.get("/health")
async def root():
    return {"message": "Hello World"}

# Upload file
@app.post("/upload")
async def create_upload_file(file: UploadFile = File(...)):
    with open(f'files/{file.filename}', "wb") as f:
        f.write(file.file.read())
    
    # Read file
    with open(f'files/{file.filename}', "r") as f:
        data = f.read()
    # Save file to database
    collection.add(
        documents=[data],
        metadatas={"filename": file.filename},
        ids=[file.filename]
    )
    return {"filename": file.filename, "message": "File uploaded successfully"}


# query file
@app.get("/docs")
def search_docs(q: str = Query(None)):
    result = collection.query(
    query_texts=q,
    n_results=2,
    )


    return {"message": "Top 2 file with the content", "result": result['metadatas']}

if __name__ == "__main__":
    client.create_collection("files")

