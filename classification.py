import sys, os, re, csv, codecs, numpy as np, pandas as pd
import threading

import matplotlib.pyplot as plt
from tkinter import messagebox
from PIL import ImageTk, Image
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation
from keras.layers import Bidirectional, GlobalMaxPool1D
from keras.models import Model
from keras import initializers, regularizers, constraints, optimizers, layers

import time
import threading

try: import tkinter
except ImportError:
    import Tkinter as tkinter
    import ttk
else: from tkinter import ttk


class MalwareClassification(object):
    def __init__(self):

        self.root = tkinter.Tk()
        self.root.geometry('320x220')
        self.root.resizable(False, False)
        self.root.configure(background="#272736")
        self.root.iconbitmap('images/icon.ico')
        self.root.title('Malware Classification')
        self.root.grid()

        self.progbar = ttk.Progressbar(self.root, length=250)
        self.progbar.config(maximum=10, mode='indeterminate')
        self.progbar.place(x=35, y=100)

        self.b_start = ttk.Button(self.root, text='Classify')
        self.b_start['command'] = self.start_thread
        self.b_start.place(x=125, y=160)

    def start_thread(self):
        self.b_start['state'] = 'Disable'
        self.progbar.start()
        self.secondary_thread = threading.Thread(target=arbitrary)
        self.secondary_thread.start()
        self.root.after(50, self.check_thread)

    def check_thread(self):
        if self.secondary_thread.is_alive():
            self.root.after(50, self.check_thread)
        else:
            self.progbar.stop()
            self.b_start['state'] = 'normal'


def classify():
    train = pd.read_csv(r'C:\Users\Aamir\PycharmProjects\MalwareDetection\\train.csv')
    test = pd.read_csv(r'C:\Users\Aamir\PycharmProjects\MalwareDetection\\test.csv')
    train.head()
    train.isnull().any(),test.isnull().any()

    list_classes = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
    y = train[list_classes].values
    list_sentences_train = train["comment_text"]
    list_sentences_test = test["comment_text"]

    max_features = 20000
    tokenizer = Tokenizer(num_words=max_features)
    tokenizer.fit_on_texts(list(list_sentences_train))
    list_tokenized_train = tokenizer.texts_to_sequences(list_sentences_train)
    list_tokenized_test = tokenizer.texts_to_sequences(list_sentences_test)

    list_tokenized_train[:1]
    maxlen = 200
    X_t = pad_sequences(list_tokenized_train, maxlen=maxlen)
    X_te = pad_sequences(list_tokenized_test, maxlen=maxlen)

    totalNumWords = [len(one_comment) for one_comment in list_tokenized_train]

    plt.hist(totalNumWords,bins = np.arange(0,410,10))#[0,50,100,150,200,250,300,350,400])#,450,500,550,600,650,700,750,800,850,900])
    plt.show()
    inp = Input(shape=(maxlen, )) #maxlen=200 as defined earlier
    embed_size = 128
    x = Embedding(max_features, embed_size)(inp)
    x = LSTM(60, return_sequences=True,name='lstm_layer')(x)
    x = GlobalMaxPool1D()(x)
    x = Dropout(0.1)(x)
    x = Dense(50, activation="relu")(x)
    x = Dropout(0.1)(x)
    x = Dense(6, activation="sigmoid")(x)


    model = Model(inputs=inp, outputs=x)
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    batch_size = 32
    epochs = 20
    model.fit(X_t,y, batch_size=batch_size, epochs=epochs, validation_split=0.1)

    model.summary()


def arbitrary():
    classify()

gui = MalwareClassification()
gui.root.mainloop()
