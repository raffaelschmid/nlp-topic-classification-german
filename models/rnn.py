
from tensorflow.keras import Sequential
import tensorflow as tf
from tensorflow.keras.layers import Dense, Conv1D, GlobalMaxPooling1D, InputLayer, Bidirectional, LSTM, RNN
from preprocessing.text import extract_vocabulary
from models.text.layers import create_text_vectorization, create_word_embedding


def build_model(X_train, y_train, output_classes, rnn_num_layers = 1, rnn_units = 32, bidirectional=True, global_max_pooling=True, activation=tf.nn.softmax, relu_activation=False):
    
    vocabulary, embedding_length = extract_vocabulary(X_train, verbose=True)
    vectorize_layer = create_text_vectorization(vocabulary)
    embedding_layer = create_word_embedding(vocabulary, embedding_length)
   
    
    model = Sequential(name="rnn")
    model.add(InputLayer(input_shape=(1,), dtype=tf.string, name="text_input"))
    model.add(vectorize_layer)
    model.add(embedding_layer)
    
    
    for layer_id in range(rnn_num_layers):
        
        return_sequences = layer_id + 1 < rnn_num_layers or global_max_pooling
       
        # return_sequences=True: required if global max pooling enabled
        layer = LSTM(rnn_units, return_sequences=return_sequences, name=f"lstm_{layer_id}")
        
        if(bidirectional):
            layer = Bidirectional(layer, name=f"bidirectional_{layer.name}")
        model.add(layer)
        
        rnn_units = int(rnn_units / 2)
    
    if(global_max_pooling):
        model.add(GlobalMaxPooling1D(name="global_max_pool"))
    
    if(relu_activation):
        model.add(Dense(rnn_units, activation=tf.nn.relu, name="relu_activation"))
    
    
    model.add(Dense(output_classes, activation=activation, name="prediction"))
    
    return (model, f"rnn_layers-{rnn_num_layers}_units-{rnn_units}")
