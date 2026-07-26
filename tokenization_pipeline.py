from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "I love AI"

#step1 : Tokenization
tokens = tokenizer.tokenize(text)

#step2 : Convert tokens to token ids
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("Original text:", text)
print("Tokens:", tokens)
print("Token IDs:", token_ids)
print("Number of tokens:", len(tokens))

#step3 : Encode the text directly to get token ids (this includes special tokens like [CLS] and [SEP])
encoded = tokenizer.encode(text)
print("Encoded IDs:", encoded)