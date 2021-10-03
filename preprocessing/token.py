import spacy
from nltk import SnowballStemmer
from fhnw.nlp.utils.text import join_tokens
from nltk import corpus

stopwords = set(corpus.stopwords.words("german"))
stemmer = SnowballStemmer("german")
lemmanizer = spacy.load("de_core_news_lg")


def ignore_stopwords(input):
    return [word for word in input if word not in stopwords]

def stem(tokens):
    return [stemmer.stem(word.lower()) for word in tokens]


def lemma(tokens):
    text = join_tokens(tokens)
    doc = lemmanizer(text, disable=['tagger', 'parser', 'ner'])
    return [tok.lemma_.lower() for tok in doc if
            tok.is_alpha and not tok.is_punct]
