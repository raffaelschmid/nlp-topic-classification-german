from nltk import word_tokenize

def tokenize(text):
    return [word.lower() for word in word_tokenize(text)]


def is_iterable(obj):
    
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def join(tokens):
    return " ".join(tokens) if is_iterable(tokens) else ""



