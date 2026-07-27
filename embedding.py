from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Text
text = "I love programming"

# Generate embedding
embedding = model.encode(text)
print("Text : ",text)
print("Embedding:", embedding)
print("Embedding dimensions:", len(embedding))