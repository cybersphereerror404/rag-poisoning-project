from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report
from ml_defense import model
from dataset import documents, labels
import numpy as np

print("=== Train/Test Split Evaluation ===")

X_train, X_test, y_train, y_test = train_test_split(
    documents,
    labels,
    test_size=0.3,
    random_state=42,
    stratify=labels
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print(classification_report(y_test, predictions))


print("\n=== 5-Fold Cross Validation ===")

scores = cross_val_score(model, documents, labels, cv=5)

print("Cross-validation scores:", scores)
print("Average accuracy:", np.mean(scores))