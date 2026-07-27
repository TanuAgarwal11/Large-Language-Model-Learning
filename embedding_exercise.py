from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2");

# Sentences
sentences = [
    "I love programming",
    "I enjoy coding",
    "I like eating pizza"
]

# Generate embeddings
embeddings = model.encode(sentences)

for sentence , embedding in zip(sentences, embeddings):
    print("\nSentence : ",sentence)
    print("Embedding Dimensions : ", len(embedding))