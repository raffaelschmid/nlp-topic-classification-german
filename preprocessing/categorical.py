from sklearn.preprocessing import LabelBinarizer

def binarizer(y_train):
    label_binarizer = LabelBinarizer()
    label_binarizer.fit(y_train)
    return label_binarizer