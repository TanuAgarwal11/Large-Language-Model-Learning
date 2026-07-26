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

#convert tokens to token ids ---- (it return 5 ids start of sequence , token ids , end of sequence)
# #Easy way to remember:
# CLS → Classification → Start of input
# SEP → Separator → Separates/ends sentences

token_ids = tokenizer.encode(text)
print("Token IDs:", token_ids) 