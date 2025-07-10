import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.IndexFlatL2(384)  # 384 dims for this model
        self.metadata = []  # Stores chunk metadata

    def add_documents(self, docs):
        print(f"Indexing {len(docs)} chunks...")
        texts = [doc['text'] for doc in docs]
        embeddings = self.model.encode(texts, batch_size=8, show_progress_bar=True)
        for doc, embedding in zip(docs, embeddings):
            self.index.add(np.array([embedding], dtype=np.float32))
            self.metadata.append(doc['metadata'])

    def search(self, query, top_k=3):
        query_emb = self.model.encode([query])
        D, I = self.index.search(np.array(query_emb, dtype=np.float32), top_k)
        results = []
        for idx in I[0]:
            # Check for invalid index (e.g., -1 or out of range)
            if idx < 0 or idx >= len(self.metadata):
                continue
            meta = self.metadata[idx]
            results.append(meta)
        return results