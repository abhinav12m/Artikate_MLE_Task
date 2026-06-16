import joblib

model = joblib.load("model.pkl")

VALID_CLASSES = {
"billing",
"technical_issue",
"feature_request",
"complaint",
"other",
}

def predict_ticket(text):
prediction = model.predict([text])[0]
return prediction

if **name** == "**main**":

```
text = "I was charged twice for my subscription"

print(predict_ticket(text))
```
