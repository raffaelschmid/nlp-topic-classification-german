from preprocessing.http import download
import fasttext as fasttext
from preprocessing.http import download


class Predictor:
    def __init__(self):
        pretrained_model = "../../data/models/fasttext.lid.176.ftz"
        download(f"https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz", pretrained_model)
        self.model = fasttext.load_model(pretrained_model)
        
    def predict(self, text):
        """Predicts the language of a sentence

        Parameters
        ----------
        text : str
            The text to predict the language

        Returns
        -------
        str
            The predicted language (e.g. en, de, ...)
        """

        lang = self.model.predict(text)[0]
        return str(lang)[11:13]