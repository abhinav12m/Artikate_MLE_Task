import json
import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

model = joblib.load("model.pkl")

df = pd.read_csv("data/manual_eval.csv")

X = df["text"]
y = df["label"]

predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)

report = classification_report(
    y,
    predictions,
    output_dict=True,
)

cm = confusion_matrix(y, predictions)

print(f"\nAccuracy: {accuracy:.4f}\n")

print(classification_report(y, predictions))

print("\nConfusion Matrix:\n")
print(cm)

with open("metrics.json", "w") as f:
    json.dump(
        {
            "accuracy": accuracy,
            "classification_report": report,
            "confusion_matrix": cm.tolist(),
        },
        f,
        indent=2,
    )

print("\nSaved metrics.json")