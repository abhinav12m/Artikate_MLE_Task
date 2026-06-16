from src.pipeline import LegalRAG

pipeline = LegalRAG()

test_cases = [
    {
        "question": "What is the notice period in Vendor X NDA?",
        "gold_doc": "nda_vendor_x.pdf",
    },
    {
        "question": "What is the liability cap in Vendor X NDA?",
        "gold_doc": "nda_vendor_x.pdf",
    },
    {
        "question": "Which agreement contains INR 1 crore liability?",
        "gold_doc": "nda_vendor_x.pdf",
    },
    {
        "question": "What is the notice period in Vendor Y agreement?",
        "gold_doc": "msa_vendor_y.pdf",
    },
    {
        "question": "What is the liability cap in Vendor Y agreement?",
        "gold_doc": "msa_vendor_y.pdf",
    },
    {
        "question": "Which agreement contains INR 2 crore liability?",
        "gold_doc": "msa_vendor_y.pdf",
    },
    {
        "question": "How long is user data retained?",
        "gold_doc": "privacy_policy.pdf",
    },
    {
        "question": "Can users request deletion of their data?",
        "gold_doc": "privacy_policy.pdf",
    },
    {
        "question": "Which document discusses user rights?",
        "gold_doc": "privacy_policy.pdf",
    },
    {
        "question": "Which agreement requires 30 days notice?",
        "gold_doc": "nda_vendor_x.pdf",
    },
]

correct = 0

for test in test_cases:

    result = pipeline.query(test["question"])

    found = any(
        source["document"] == test["gold_doc"]
        for source in result["sources"]
    )

    if found:
        correct += 1

precision_at_3 = correct / len(test_cases)

print("=" * 50)
print(f"Correct Retrievals: {correct}")
print(f"Total Questions: {len(test_cases)}")
print(f"Precision@3: {precision_at_3:.2f}")
print("=" * 50)