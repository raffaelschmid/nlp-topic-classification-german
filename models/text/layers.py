from keras.layers import TextVectorization
from tensorflow.keras.layers import Embedding
import numpy as np
import fasttext


def create_text_vectorization(vocabulary):
    return TextVectorization(
        output_mode='int',
        output_sequence_length=None,
        vocabulary=list(vocabulary),
        name="text_vectorization"
    )


def get_embedder_fasttext(embedding_dim, model_name="cc.de.300.bin"):
    split = model_name.split(".")
    model_lang = split[1]
    model_dim = int(split[2])

    try:
        ft = fasttext.load_model(model_name)
    except ValueError:
        fasttext.util.download_model(model_lang, if_exists='ignore')
        ft = fasttext.load_model(model_name)

    if embedding_dim < model_dim:
        fasttext.util.reduce_model(ft, embedding_dim)

    def fasttext_embedder(word):
        return ft.get_word_vector(word)

    return fasttext_embedder


def calculate_embedding_matrix(vocabulary, embedding_dim=300, verbose=False):
    """Creates the embedding matrix
    """
    voc_size = len(vocabulary)
    words_not_found = set()
    embedding_matrix = np.zeros((voc_size, embedding_dim))

    embedder = get_embedder_fasttext(embedding_dim)
    
    
    for idx, word in enumerate(vocabulary):
        embedding_vector = embedder(word)
        if (embedding_vector is not None) and len(embedding_vector) > 0 and not np.all(embedding_vector == 0):
            # words not found in embedding index will be all-zeros.
            embedding_matrix[idx] = embedding_vector
        else:
            words_not_found.add(word)

    if verbose:
        print("Embedding type: fasttext")
        print("Number of null word embeddings:", np.sum(np.sum(embedding_matrix, axis=1) == 0))
        nr_words_not_found = len(words_not_found)
        print("Words not found in total:", len(words_not_found))
        if nr_words_not_found > 0:
            import random

            nr_sample = min(20, len(words_not_found))
            print("Words without embedding (", nr_sample, "/", nr_words_not_found, "): ",
                  random.sample(words_not_found, nr_sample), sep='')

    return embedding_matrix


def create_word_embedding(vocabulary, embedding_length):
    embedding_matrix = calculate_embedding_matrix(vocabulary)
    embedding_layer = Embedding(
        embedding_matrix.shape[0],
        embedding_matrix.shape[1],
        weights=[embedding_matrix],
        input_length=embedding_length,
        trainable=False,
        mask_zero=True,
        name="embedding"
    )