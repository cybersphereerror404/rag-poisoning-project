from rag_engine import index_document, query_system
from attack import generate_poisoned_document
from ml_defense import ml_detect
from consistency_filter import consistency_filter

# Safe document
safe_doc = "Cybersecurity involves protecting networks and systems."

# Poisoned document
poisoned_doc = generate_poisoned_document()

documents = [safe_doc, poisoned_doc]

print("=== WITH ML DEFENSE ===")

# Apply ML defense before indexing
for doc in documents:
    result = ml_detect(doc)
    print(f"Document risk score: {result['risk_score']:.3f}")
    
    if result["status"] == "ML classified as safe":
        index_document(doc)
        print("Indexed.")
    else:
        print("Blocked by ML defense.")

# Query system
retrieved_docs = query_system("What does cybersecurity involve?")

filtered_docs = consistency_filter(retrieved_docs)

print("\nAfter Consistency Filtering:")
for doc in filtered_docs:
    print("-", doc)

final_answer = filtered_docs[0]

print("\nFinal Response:")
print(final_answer)
