# function to count tokens
def count_words(text) : 
   words = text.split()
   print("words", words)
   print("Number of tokens in text : ", len(words))
    
text = "I am learning LLM"
count_words(text)

