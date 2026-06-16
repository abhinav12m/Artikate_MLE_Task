import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data/tickets.csv")

X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
stratify=y,
random_state=42
)

pipeline = Pipeline([
("tfidf", TfidfVectorizer()),
("clf", LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "model.pkl")

print("Model saved.")
