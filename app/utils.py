from pathlib import Path
import fitz  # PyMuPDF
import docx

def extract_pdf_text(filepath):
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_docx_text(filepath):
    doc = docx.Document(filepath)
    return "\n".join([para.text for para in doc.paragraphs])

def load_documents(doc_dir):
    docs = []
    for file in Path(doc_dir).glob("*"):
        if file.suffix == ".pdf":
            text = extract_pdf_text(file)
        elif file.suffix == ".docx":
            text = extract_docx_text(file)
        else:
            continue
        docs.append({"filename": file.name, "text": text})
    return docs

def chunk_text(text, chunk_size=300, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks
