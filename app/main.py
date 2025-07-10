from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.rag import answer_query

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_endpoint(request: QueryRequest):
    try:
        result = answer_query(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Welcome to the RAG API. Use the /query endpoint to ask questions."}