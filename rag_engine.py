from ml_detector import ml_detect


def filter_retrieved_docs(documents, top_indices):
    retrieved_docs = [documents[i] for i in top_indices]

    safe_docs = []

    for doc in retrieved_docs:
        result = ml_detect(doc)

        if result["risk_score"] < 0.5:
            safe_docs.append(doc)
        else:
            print("Blocked poisoned document:", doc)

    print("Top retrieved documents:")
    for doc in retrieved_docs:
        print("-", doc)

    return safe_docs