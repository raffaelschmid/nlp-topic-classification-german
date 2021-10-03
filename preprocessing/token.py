import string

import spacy
from nltk import SnowballStemmer
from fhnw.nlp.utils.text import join_tokens
from nltk import corpus

stopwords = set(corpus.stopwords.words("german"))
lemmanizer = spacy.load("de_core_news_lg")
stemmer = SnowballStemmer("german")
punctuation = r"""!"#$%&'()*+,-–./:;<=>?@[\]^_`{|}~"""


def ignore_stopwords(input):
    return [word for word in input if word not in stopwords]


def stem(tokens):
    return [stemmer.stem(word.lower()) for word in tokens if word not in punctuation]


def lemma(tokens):
    text = join_tokens(tokens)
    doc = lemmanizer(text, disable=['tagger', 'parser', 'ner'])
    # do not check is_alpha because of 21-jähriger
    return [tok.lemma_.lower() for tok in doc if not tok.is_punct]
