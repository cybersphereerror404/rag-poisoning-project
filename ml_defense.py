# ml_defense.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from dataset import documents, labels


# ===============================
# Split dataset for evaluation
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    documents,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)


# ===============================
# Build ML Pipeline
# ===============================

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1,2),
        max_features=5000,
        stop_words="english"
    )),
    ("clf", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])


# ===============================
# Train Model
# ===============================

model.fit(X_train, y_train)


# ===============================
# Evaluate Model
# ===============================

y_pred = model.predict(X_test)

print("ML Defense Evaluation")
print("---------------------")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


# ===============================
# Detection Function
# ===============================

def ml_detect(text, threshold=0.43):
    """
    Detects prompt injection risk using trained ML classifier
    """

    probability = float(model.predict_proba([text])[0][1])

    if probability >= threshold:
        return {
            "risk_score": round(probability, 4),
            "status": "ML detected malicious content"
        }

    return {
        "risk_score": round(probability, 4),
        "status": "ML classified as safe"
    }

   