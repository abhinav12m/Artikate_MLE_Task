# Artikate Studio – Assessment

The assessment consists of:

* Section 1 – Diagnose a Failing LLM Pipeline
* Section 2 – Production-Grade Legal RAG Pipeline
* Section 3 – Customer Support Ticket Classifier
* Section 4 – Written Systems Design Review

---

# Repository Structure

```text
.
├── README.md
├── ANSWERS.md
├── DESIGN.md
├── requirements.txt
│
├── Sec2/
│   ├── data/
│   ├── src/
│   ├── ingest_once.py
│   ├── run.py
│   └── evaluate.py
│
└── Sec3/
    ├── data/
    ├── generate_data.py
    ├── train.py
    ├── predict.py
    ├── evaluate.py
    └── latency_test.py
```

---

# Setup

## 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Section 1 – Diagnose a Failing LLM Pipeline

Written responses covering:

* Hallucinated pricing
* Language switching
* Latency degradation
* Post-mortem summary

See:

```text
ANSWERS.md
```

---

# Section 2 – Production-Grade Legal RAG Pipeline

Implemented features:

* PDF ingestion
* Recursive chunking
* Embedding generation
* ChromaDB vector storage
* Semantic retrieval
* Source citation
* Confidence scoring
* Hallucination mitigation

## Build Vector Store

```bash
cd Sec2

python ingest_once.py
```

## Run Example Query

```bash
python run.py
```

Example query:

```python
result = pipeline.query(
    question="What is the notice period in the NDA with Vendor X?"
)
```

## Run Evaluation

```bash
python evaluate.py
```

Result:

```text
Correct Retrievals: 9
Total Questions: 10
Precision@3: 0.90
```

Additional design decisions are documented in:

```text
DESIGN.md
```

---

# Section 3 – Ticket Classification

Implemented using:

* TF-IDF
* Logistic Regression
* Scikit-Learn

## Generate Dataset

```bash
cd Sec3

python generate_data.py
```

## Train Model

```bash
python train.py
```

## Evaluate Model

```bash
python evaluate.py
```

Observed Results:

```text
Accuracy: 0.90
```

Per-Class F1:

| Class           | F1 Score |
| --------------- | -------- |
| billing         | 1.00     |
| complaint       | 0.82     |
| feature_request | 1.00     |
| other           | 1.00     |
| technical_issue | 0.77     |

## Run Latency Test

```bash
python latency_test.py
```

Observed Result:

```text
Latency: 2.13 ms
Latency test passed.
```

---

# Section 4 – Systems Design Review

Written answers covering:

* Prompt Injection & LLM Security
* Evaluating LLM Output Quality

See:

```text
ANSWERS.md
```

---

# Documentation

### DESIGN.md

Contains:

* Chunking strategy
* Embedding model choice
* Vector store selection
* Retrieval strategy
* Hallucination mitigation
* Evaluation methodology
* Scaling considerations

### ANSWERS.md

Contains:

* Section 1 written responses
* Section 3 model selection and evaluation discussion
* Section 4 systems design answers

---

# Technologies Used

* Python
* ChromaDB
* Sentence Transformers
* Scikit-Learn
* Logistic Regression
* TF-IDF
* PyMuPDF
* LangChain Text Splitters

---

# Notes

* No external APIs are required.
* No API keys are required.
* All code runs locally.
* The implementation prioritizes simplicity, reproducibility, and clear evaluation.


# Acknowledgements

AI-assisted tools were used during the completion of this assessment for productivity and learning purposes, including:

* Brainstorming and discussion of architectural trade-offs
* Assistance with debugging and resolving implementation issues
* Generation of synthetic training data for Section 3
* Drafting and refinement of documentation files such as README.md, DESIGN.md, and ANSWERS.md
* Reviewing code structure and evaluation methodology

All design decisions, implementation choices, evaluation results, and final submitted content were reviewed, modified where necessary, and validated by me before submission.
