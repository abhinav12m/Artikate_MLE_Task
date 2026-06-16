import chromadb

from sentence_transformers import SentenceTransformer

from src.ingest import load_documents


class LegalRAG:

    def __init__(self):

        self.embedder = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            "legal_docs"
        )

    def ingest(self):

        chunks = load_documents()

        for idx, chunk in enumerate(chunks):

            embedding = self.embedder.encode(
                chunk["text"]
            ).tolist()

            self.collection.add(
                ids=[str(idx)],
                embeddings=[embedding],
                documents=[chunk["text"]],
                metadatas=[
                    {
                        "document": chunk["document"],
                        "page": chunk["page"],
                    }
                ],
            )

    def query(self, question):

        query_embedding = self.embedder.encode(
            question
        ).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=3,
        )

        docs = results["documents"][0]
        metas = results["metadatas"][0]
        distances = results["distances"][0]

        best_distance = distances[0]

        confidence = round(
            max(0.0, 1 - best_distance),
            2
        )

        if confidence < 0.4:

            return {
                "answer": (
                    "Insufficient evidence found "
                    "in retrieved documents."
                ),
                "sources": [],
                "confidence": confidence,
            }

        answer = f"""
        Based on {metas[0]['document']} (Page {metas[0]['page']}),

       {docs[0]}
        """

        sources = []

        for doc, meta in zip(docs, metas):

            sources.append(
                {
                    "document": meta["document"],
                    "page": meta["page"],
                    "chunk": doc,
                }
            )

        return {
            "answer": answer,
            "sources": sources,
            "confidence": round(confidence, 2),
        }