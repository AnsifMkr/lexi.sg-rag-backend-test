from .vector_store import VectorStore
from .utils import load_documents, chunk_text

vector_store = VectorStore()
docs = load_documents("cases")

chunks = []
for doc in docs:
    chunks_list = chunk_text(doc['text'])
    for idx, chunk in enumerate(chunks_list):
        chunks.append({
            "text": chunk,
            "metadata": {
                "text": chunk,
                "source": doc['filename'],
                "chunk_id": idx
            }
        })

vector_store.add_documents(chunks)

def answer_query(query):
    citations = vector_store.search(query)
    if not citations:
        return {"answer": "No relevant documents found.", "citations": []}
    answer = "Based on the retrieved documents, " + " ".join([c['text'] for c in citations])
    citations_list = [{"text": c['text'], "source": c['source']} for c in citations]
    return {"answer": answer, "citations": citations_list}