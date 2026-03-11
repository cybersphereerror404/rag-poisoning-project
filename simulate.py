from rag_engine import index_document, query_system
from attack import generate_poisoned_document
from defense import detect_poisoning_from_text

# Safe document
safe_doc = "Cybersecurity involves protecting networks and systems."

# Poisoned document
poisoned_doc = generate_poisoned_document()

# ---- DEFENSE CHECK ----
if detect_poisoning_from_text(poisoned_doc)["risk_score"] == 0:
    index_document(poisoned_doc)
else:
    print("Poisoned document blocked.")

# Always index safe document
index_document(safe_doc)

# Query system
response = query_system("cybersecurity")

print("Retrieved Document:")
print(response)