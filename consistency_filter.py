from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def detect_keyword_attack(doc):
    suspicious_terms = ["ignore", "delete", "override", "bypass"]
    for term in suspicious_terms:
        if term in doc.lower():
            return True
    return False


def semantic_outlier_filter(docs):
    if len(docs) <= 1:
        return docs

    embeddings = embedder.encode(docs)
    similarity_matrix = cosine_similarity(embeddings)

    avg_similarities = []

    for i in range(len(docs)):
        # average similarity to other docs
        avg_sim = np.mean(np.delete(similarity_matrix[i], i))
        avg_similarities.append(avg_sim)

    # keep documents that are close to majority
    threshold = np.mean(avg_similarities) - 0.1

    filtered_docs = [
        docs[i] for i in range(len(docs))
        if avg_similarities[i] >= threshold
    ]

    return filtered_docs


def consistency_filter(retrieved_docs):
    # Remove obvious keyword attacks first
    docs_no_keywords = [
        doc for doc in retrieved_docs
        if not detect_keyword_attack(doc)
    ]

    if not docs_no_keywords:
        docs_no_keywords = retrieved_docs

    # Apply semantic filtering
    final_docs = semantic_outlier_filter(docs_no_keywords)

    return final_docs