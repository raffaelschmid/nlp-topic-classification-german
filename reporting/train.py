import matplotlib.pyplot as plt

def plot_history(history, fig_size=(10,5)):
    """Plots the history of a training run

    Parameters: 
        history: history
            The history to plot
    """
    f_acc, ax_acc = plt.subplots(figsize=fig_size)
    ax_acc.plot(history.history['accuracy'], label='train')
    ax_acc.plot(history.history['val_accuracy'], label='test')
    ax_acc.legend()
    ax_acc.grid(True)
    ax_acc.set_xlabel("epoche")
    ax_acc.set_ylabel("accuracy")

    f_loss, ax_loss = plt.subplots(figsize=fig_size)
    ax_loss.plot(history.history['loss'], label='train')
    ax_loss.plot(history.history['val_loss'], label='test')
    ax_loss.legend()
    ax_loss.grid(True)
    ax_loss.set_xlabel("epoche")
    ax_loss.set_ylabel("loss")
    
    
    