from src.pipeline import LegalRAG

pipeline = LegalRAG()
pipeline.ingest()

print("Documents ingested successfully.")