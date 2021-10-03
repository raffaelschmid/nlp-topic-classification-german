import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud


def create_word_cloud(df):
    """Creates a wordcloud of a column of text

    Parameters
    ----------
    df : dataframe
        The dataframe
    field : str
        The column name to read from (default is token_lemma)
    """

    counter = Counter()
    _ = df.apply(counter.update)

    wc = WordCloud(background_color="white", max_words=1000)
    wc.generate_from_frequencies(counter)

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
