from src.pipeline import LegalRAG

pipeline = LegalRAG()

result = pipeline.query(
    "What is the notice period in the NDA with Vendor X?"
)

print(result)