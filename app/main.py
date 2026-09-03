from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File 
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from ingestion import extract_text, chunk_text
from vectorstore import add_chunks, search_chunks
from rag import generate_answer

app = FastAPI(title="Document Intelligence API")

# Serve frontend
frontend_path = Path(__file__).parent.parent / "frontend"
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

class QueryRequest(BaseModel):
    question: str 
    top_k: int = 4

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text(file.filename, contents)
    chunks = chunk_text(text)
    n = add_chunks(doc_id=file.filename, chunks=chunks)
    return {"filename": file.filename, "chunks_created": n}

@app.post("/query")
async def query_documents(request: QueryRequest):
    results = search_chunks(request.question, top_k=request.top_k)
    return generate_answer(request.question, results)
