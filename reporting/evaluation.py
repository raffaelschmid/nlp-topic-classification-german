import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
from seaborn import heatmap
from sklearn.metrics import confusion_matrix


def plot_confusion_matrix(y_true, y_pred, figsize=(10, 10)):
    """
    Plots confusion matrix containing percentage
    """
    cm = confusion_matrix(y_true, y_pred, labels=np.unique(y_true))
    cm_sum = np.sum(cm, axis=1, keepdims=True)
    cm_perc = cm / cm_sum.astype(float) * 100
    annot = np.empty_like(cm).astype(str)
    nrows, ncols = cm.shape
    for i in range(nrows):
        for j in range(ncols):
            c = cm[i, j]
            p = cm_perc[i, j]
            if i == j:
                s = cm_sum[i]
                annot[i, j] = '%.1f%%\n%d/%d' % (p, c, s)
            elif c == 0:
                annot[i, j] = ''
            else:
                annot[i, j] = '%.1f%%\n%d' % (p, c)
    cm = DataFrame(cm, index=np.unique(y_true), columns=np.unique(y_true))
    cm.index.name = 'Actual'
    cm.columns.name = 'Predicted'
    fig, ax = plt.subplots(figsize=figsize)
    heatmap(cm, cmap="YlGnBu", annot=annot, fmt='', ax=ax)


def percentage_confusion_matrix(y_pred, y_true):
    """
    Returns confusion matrix percentage values.
    :rtype: DataFrame
    """
    cm = confusion_matrix(y_true, y_pred, labels=np.unique(y_true))
    cm_sum = np.sum(cm, axis=1, keepdims=True)
    cm_perc = np.round(cm / cm_sum.astype(float) * 100, 3)

    p = DataFrame(cm_perc, index=np.unique(y_true), columns=np.unique(y_true))
    p.index.name = 'Actual'
    p.columns.name = 'Predicted'
    return p

def percentage_true_positives(predicted, expected, column='True Positives'):
    perc = percentage_confusion_matrix(predicted, expected)
    data = [perc[label][label] for label in perc.index]
    return DataFrame(data, index=np.unique(expected), columns=[column])
