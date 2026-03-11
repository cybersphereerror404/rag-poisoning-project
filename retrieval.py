from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_most_similar(query, documents):
    # Convert documents into embeddings
    doc_embeddings = model.encode(documents)

    # Convert query into embedding
    query_embedding = model.encode([query])

    # Compute similarity
    similarities = cosine_similarity(query_embedding, doc_embeddings)

    # Get most similar document index
    most_similar_index = np.argmax(similarities)

    return documents[most_similar_index]