from rag_engine import index_document, query_system
from attack import generate_poisoned_document

safe_doc = "Cybersecurity involves protecting networks and systems."
poisoned_doc = generate_poisoned_document()

# Simulate corpus poisoning (multiple malicious insertions)
index_document(poisoned_doc)
index_document(poisoned_doc)
index_document(poisoned_doc)

# Index safe document once
index_document(safe_doc)

response = query_system("What does cybersecurity involve?")

print("=== WITHOUT DEFENSE ===")
print("Retrieved Document:")
print(response)