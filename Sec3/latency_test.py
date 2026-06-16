import time
import joblib

VALID_CLASSES = {
"billing",
"technical_issue",
"feature_request",
"complaint",
"other",
}

tickets = [
"I was charged twice",
"Refund has not arrived",
"Export button does not work",
"Application crashes",
"Please add dark mode",
"Need Slack integration",
"Support never responds",
"Very disappointed",
"Where is the documentation",
"What are your business hours",
"Invoice amount is incorrect",
"Cannot upload files",
"Please support PDF export",
"Customer service is terrible",
"How do I contact sales",
"Unexpected charge on my account",
"Dashboard is blank",
"Need email notifications",
"Response time is unacceptable",
"Where is your office located",
]

model = joblib.load("model.pkl")

start = time.perf_counter()

predictions = model.predict(tickets)

elapsed_ms = (time.perf_counter() - start) * 1000

for prediction in predictions:
    assert prediction in VALID_CLASSES

assert elapsed_ms < 500

print(f"Latency: {elapsed_ms:.2f} ms")
print("Latency test passed.")
