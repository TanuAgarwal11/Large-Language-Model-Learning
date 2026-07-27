from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sentences
sentences = [
    "I love programming",
    "I enjoy coding",
    "I like eating pizza"
]

# Generate embeddings
embeddings = model.encode(sentences)

# Calculate semantic similarity
similarity = cosine_similarity(embeddings)

print(similarity)