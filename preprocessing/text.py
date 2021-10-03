from nltk import word_tokenize

def tokenize(text):
    return [word.lower() for word in word_tokenize(text)]


