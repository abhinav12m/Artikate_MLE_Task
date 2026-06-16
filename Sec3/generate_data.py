import random
import pandas as pd

random.seed(42)

data = []

# -------------------------

# Billing

# -------------------------

products = [
"subscription",
"premium plan",
"enterprise plan",
"monthly package",
]

months = [
"January",
"February",
"March",
"April",
]

billing_templates = [
"I was charged twice for my {product} in {month}",
"Why was I billed again for the {product}?",
"My refund for the {product} has not arrived",
"The invoice amount for my {product} is incorrect",
"I noticed an unexpected charge on my account",
]

# -------------------------

# Technical

# -------------------------

actions = [
"login",
"upload files",
"download reports",
"export CSV",
"reset my password",
]

technical_templates = [
"I cannot {action}",
"{action} is not working",
"The application crashes when I try to {action}",
"I receive an error while trying to {action}",
"{action} keeps failing",
]

# -------------------------

# Feature Requests

# -------------------------

features = [
"dark mode",
"Slack integration",
"PDF export",
"email notifications",
"mobile app support",
]

feature_templates = [
"Please add {feature}",
"Can you support {feature}?",
"I would like {feature}",
"It would be helpful to have {feature}",
"Can {feature} be added in a future release?",
]

# -------------------------

# Complaints

# -------------------------

issues = [
"the application crashes frequently",
"support never replies",
"the product is unreliable",
"the service is too slow",
"the dashboard keeps breaking",
]

complaint_templates = [
"I am very frustrated because {issue}",
"This has been a terrible experience",
"I am disappointed with the service",
"Your support team has been unhelpful",
"The quality of the product is unacceptable",
]

# -------------------------

# Other

# -------------------------

other_templates = [
"Where can I find documentation?",
"What are your business hours?",
"How do I contact sales?",
"Do you offer enterprise pricing?",
"Where is your company located?",
]

# -------------------------

# Generate 200 per class

# -------------------------

for _ in range(200):

    data.append({
        "text": random.choice(billing_templates).format(
            product=random.choice(products),
            month=random.choice(months)
        ),
        "label": "billing"
    })

    data.append({
        "text": random.choice(technical_templates).format(
            action=random.choice(actions)
        ),
        "label": "technical_issue"
    })

    data.append({
        "text": random.choice(feature_templates).format(
            feature=random.choice(features)
        ),
        "label": "feature_request"
    })

    data.append({
        "text": random.choice(complaint_templates).format(
            issue=random.choice(issues)
        ),
        "label": "complaint"
    })

    data.append({
        "text": random.choice(other_templates),
        "label": "other"
    })

df = pd.DataFrame(data)

df = df.sample(frac=1, random_state=42)

df.to_csv("data/tickets.csv", index=False)

print(df.head())
print()
print(df["label"].value_counts())
print()
print(f"Dataset size: {len(df)}")