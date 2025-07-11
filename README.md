# lexi.sg-rag-backend-test

✅ **Retrieval-Augmented Generation (RAG) Backend for Legal Document Question Answering**  
This project implements a backend service that accepts natural language legal queries and returns:
- A generated answer based on retrieved documents  
- A list of citations from original legal documents (PDF/DOCX)

---

## 🚀 Features
- Document Parsing: Supports both **PDF** and **DOCX** files
- Embedding: Uses free **Sentence-Transformers** model (`all-MiniLM-L6-v2`)
- Vector Store: Uses **FAISS** for efficient vector similarity search
- API: Provides `/query` endpoint via **FastAPI**
- Citation Support: Returns sources and chunk IDs from documents 
