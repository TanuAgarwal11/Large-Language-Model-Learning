from transformers import AutoTokenizer
# Load a tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = input("Enter your message :")

#convert text into tokens
tokens = tokenizer.tokenize(text)

print("Original Text : ", text)
print("Tokens : ", tokens)

# convert tokens into token ids
token_ids = tokenizer.encode(text)

print("Token IDs : ", token_ids)
print("Number of tokens : ",len(tokens))