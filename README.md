# Legal RAG Pipeline

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline for answering questions over legal documents.

The system supports:

* PDF ingestion
* Chunking
* Embedding generation
* Vector storage using ChromaDB
* Semantic retrieval
* Source citation
* Confidence scoring
* Evaluation using Precision@3

---

## Project Structure

```text
.
├── data/
│   ├── nda_vendor_x.pdf
│   ├── msa_vendor_y.pdf
│   └── privacy_policy.pdf
│
├── src/
│   ├── ingest.py
│   └── pipeline.py
│
├── run.py
├── evaluate.py
├── DESIGN.md
├── README.md
└── requirements.txt
```

---

## Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Document Ingestion

The sample legal documents are located in the `data/` folder.

To create embeddings and populate the vector database:

```bash
python ingest_once.py
```

This will create the local ChromaDB database.

---

## Run a Query

Execute:

```bash
python run.py
```

Example query:

```python
result = pipeline.query(
    "What is the notice period in the NDA with Vendor X?"
)
```

Example output:

```python
{
    "answer": "...",
    "sources": [
        {
            "document": "nda_vendor_x.pdf",
            "page": 1,
            "chunk": "..."
        }
    ],
    "confidence": 0.62
}
```

---

## Run Evaluation

Evaluate retrieval quality using Precision@3:

```bash
python evaluate.py
```

Example output:

```text
Correct Retrievals: 9
Total Questions: 10
Precision@3: 0.90
```

---

## Design Decisions

Detailed architectural decisions and trade-offs are documented in:

```text
DESIGN.md
```

This includes:

* Chunking strategy
* Embedding model choice
* Vector store selection
* Retrieval strategy
* Hallucination mitigation
* Scaling considerations
* Evaluation methodology

---

## Technologies Used

* Python
* ChromaDB
* Sentence Transformers
* BAAI/bge-small-en-v1.5
* PyMuPDF
* LangChain Text Splitters

```
```
