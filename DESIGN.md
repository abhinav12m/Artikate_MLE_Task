# DESIGN.md

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline for answering questions over legal documents such as contracts and policies.

The system supports:

* PDF ingestion
* Chunking
* Embedding generation
* Vector search
* Source citation
* Confidence scoring
* Evaluation using Precision@3

The primary goal is to provide grounded answers with document and page references while minimizing hallucinations.

---

## Chunking Strategy

Legal clauses often span multiple sentences, so splitting documents too aggressively can separate important context.

I used LangChain's `RecursiveCharacterTextSplitter` with:

* Chunk size: 500 characters
* Chunk overlap: 100 characters

The overlap helps preserve context across chunk boundaries and improves retrieval quality.

For a larger production system, I would use section-aware chunking based on clause and section headers to better preserve legal structure.

---

## Embedding Model Choice

**Model:** `BAAI/bge-small-en-v1.5`

Reasons:

* Strong semantic retrieval performance
* Open source
* No API costs
* Lightweight and easy to run locally

I chose BGE Small over larger models because it provides a good balance between retrieval quality and ease of deployment.

---

## Vector Store Choice

**Vector Database:** ChromaDB

Reasons:

* Persistent local storage
* Metadata support
* Simple setup
* No external infrastructure required

I considered FAISS and Pinecone. FAISS is fast but offers limited metadata support, while Pinecone is better suited for large-scale production deployments. For a corpus of roughly 60,000 chunks, ChromaDB is sufficient.

---

## Retrieval Strategy

The system uses dense vector retrieval.

Process:

1. Convert the query into an embedding
2. Retrieve the Top-3 most similar chunks from ChromaDB
3. Return the highest-ranked chunk as the answer
4. Return retrieved chunks as source citations

I selected dense retrieval because it is simple, effective, and easy to reproduce locally.

For a production legal search system, I would use:

* Hybrid retrieval (BM25 + dense retrieval)
* Cross-encoder re-ranking

to improve precision on legal terminology and clause references.

---

## Hallucination Mitigation

Hallucinated legal answers can be misleading and potentially harmful.

To reduce hallucinations:

* Answers are generated only from retrieved document chunks
* A confidence score is calculated using retrieval distance
* If confidence is too low, the system returns:

> "Insufficient evidence found in retrieved documents."

This approach favors refusing to answer over providing unsupported information.

---

## Evaluation

I created 10 manual question-answer pairs covering:

* Notice periods
* Liability limits
* Data retention policies
* User rights

The retrieval system was evaluated using Precision@3.

### Results

| Metric                      | Score |
| --------------------------- | ----- |
| Total Questions             | 10    |
| Correct Retrievals in Top-3 | 9     |
| Precision@3                 | 0.90  |

This means the correct supporting document was retrieved within the top three results for 90% of evaluation queries.

---

## Scaling to 50,000 Documents

If the corpus grows from 500 documents to 50,000 documents, the main bottlenecks become:

### Vector Search

ChromaDB may not scale efficiently to millions of chunks.

**Solution:** Move to Pinecone, Qdrant, or Weaviate with ANN indexing (HNSW).

### Embedding Generation

Generating embeddings for millions of chunks becomes expensive.

**Solution:** Batch processing and distributed ingestion pipelines.

### Retrieval Quality

More documents increase retrieval ambiguity.

**Solution:** Hybrid retrieval, metadata filtering, and re-ranking.

### Metadata Search

Queries often reference specific vendors or contract types.

**Solution:** Combine metadata filtering with vector search to narrow the search space.

---

## Conclusion

This implementation prioritizes:

* Simplicity
* Reproducibility
* Source attribution
* Hallucination resistance

while remaining easy to run locally and extensible to larger production-scale document repositories.