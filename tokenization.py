from transformers import AutoTokenizer

# Load a tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Our text
text = "I love AI"

# Convert text into tokens
tokens = tokenizer.tokenize(text)

print("Original text:", text)
print("Tokens:", tokens)
print("Number of tokens:", len(tokens))