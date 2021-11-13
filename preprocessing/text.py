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




def extract_vocabulary(data, verbose=False, sequence_length_percentil_cutoff = 0.98, sequence_length_max = 768):

    vocabulary = set()
    _ = data.apply(lambda x: vocabulary.update(x))

    lengths = data.apply(len)
    max_sequence_length = int(lengths.quantile(1.0))
    percentil_sequence_length = int(lengths.quantile(0.98))
    median_sequence_length = int(lengths.quantile(0.5))
    embedding_length = min(sequence_length_max, percentil_sequence_length)

    if verbose:
        print(f"Median sequence length:       : {median_sequence_length}")
        print(f"Percentil                     : {sequence_length_percentil_cutoff})")
        print(f"Cutoff sequence length        : {percentil_sequence_length}")
        print(f"Max sequence length           : {max_sequence_length}")
        print(f"Embedding length              : {embedding_length}")
        print(f"Vocabulary length             : {len(vocabulary)}")

    return (vocabulary, embedding_length)