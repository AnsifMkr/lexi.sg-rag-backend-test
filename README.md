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

```bash
# Clone the repository
git clone https://github.com/AnsifMkr/lexi.sg-rag-backend-test.git
cd lexi.sg-rag-backend-test

# (Optional) Setup virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the server
```
uvicorn app.main:app --reload
```

### API 
GET http://127.0.0.1:8000/

```
{
  "message": "Welcome to the RAG API. Use the /query endpoint to ask questions."
}
```
POST http://127.0.0.1:8000/query
```
{"query": "Is an insurance company liable to pay compensation if a transport vehicle involved in an accident was being used without a valid permit?"}
```
```
{
  "answer": "Based on the retrieved documents,  the Appellants :- Abhishek Atrey, Advocate. \nFor the Respondents :- Amit Kumar Singh, Advocate. \nMotor Vehicles Act, 1988 Sections 166, 66 and 149 Accident - No permit - Liability to pay compensation - Vehicle at time of accident did not have permit - Use of vehicle in public place without permit i apart, a stand was taken that the vehicle did not have the permit on the date of the accident. On behalf of the owner of the vehicle and driver, assertions were made that the vehicle was insured with the first respondent as per the insurance policy, that the vehicle was registered and the driver had s found that the accident was caused solely because of some other unforeseen or intervening causes like mechanical failures and similar other causes having no nexus with the driver not possessing the requisite type of licence, the insurer will not be allowed to avoid its liability merely for technic",
  "citations": [
    {
      "text": " the Appellants :- Abhishek Atrey, Advocate. \nFor the Respondents :- Amit Kumar Singh, Advocate. \nMotor Vehicles Act, 1988 Sections 166, 66 and 149 Accident - No permit - Liability to pay compensation - Vehicle at time of accident did not have permit - Use of vehicle in public place without permit i",
      "source": "Amrit Paul Singh v. TATA AIG (SC NO ROUTE Permit insurance Co. Recover from Owner).docx"
    },
    {
      "text": "apart, a stand was taken that the vehicle did not have the permit on the date of the accident. On behalf of the owner of the vehicle and driver, assertions were made that the vehicle was insured with the first respondent as per the insurance policy, that the vehicle was registered and the driver had",
      "source": "Amrit Paul Singh v. TATA AIG (SC NO ROUTE Permit insurance Co. Recover from Owner).docx"
    },
    {
      "text": "s found that the accident was caused solely because of some other unforeseen or intervening causes like mechanical failures and similar other causes having no nexus with the driver not possessing the requisite type of licence, the insurer will not be allowed to avoid its liability merely for technic",
      "source": "Amrit Paul Singh v. TATA AIG (SC NO ROUTE Permit insurance Co. Recover from Owner).docx"
    }
  ]
}
```
