from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
import pickle
import joblib
pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn import tree, linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import sklearn.ensemble as ske
import time
import threading

try: import tkinter
except ImportError:
    import Tkinter as tkinter
    import ttk
else: from tkinter import ttk

class Malware_Detection(object):
    def __init__(self):

        self.root = tkinter.Tk()
        self.root.geometry('320x220')
        self.root.resizable(False, False)
        self.root.configure(background="#272736")
        self.root.iconbitmap('images/icon.ico')
        self.root.title('Malware Detection')
        self.root.grid()

        self.progbar = ttk.Progressbar(self.root, length=250)
        self.progbar.config(maximum=10, mode='indeterminate')
        self.progbar.place(x=35, y=100)

        self.b_start = ttk.Button(self.root, text='Detect')
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


def detect():
    data = pd.read_csv("dynamic_api_call_sequence_per_malware_100_0_306.csv")

    data.head(5)

    data.shape

    data.describe()

    # scaler = MinMaxScaler()
    # scaledata = scaler.fit_transform()

    from sklearn import preprocessing
    le = preprocessing.LabelEncoder()

    le.fit(['A', 'B', 'C', 'A', 'E', 'F', 'C', 'A', 'D'])

    print(le.classes_)

    le.transform(['A', 'B', 'C', 'C', 'A', 'F'])

    X = data.drop(['hash', 'malware'], axis=1).values
    Y = data['malware'].values

    scaler = MinMaxScaler()
    x = scaler.fit_transform(X)

    x

    X_train, X_test, y_train, y_test = train_test_split(x, Y, test_size=0.2)

    X_train

    X_test

    y_test

    y_train

    algorithms = {
        "DecisionTree": tree.DecisionTreeClassifier(max_depth=10),
        "RandomForest": ske.RandomForestClassifier(n_estimators=50),
        "GradientBoosting": ske.GradientBoostingClassifier(n_estimators=50),
        "AdaBoost": ske.AdaBoostClassifier(n_estimators=100),
        "GNB": GaussianNB()
    }

    results = {}
    print("\nNow testing algorithms")
    for algo in algorithms:
        clf = algorithms[algo]
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        print("%s : %f %%" % (algo, score * 100))
        results[algo] = score

    classifier = ske.RandomForestClassifier(n_estimators=100)
    classifier.fit(X_train, y_train)

    ypred = classifier.predict(X_test)

    ypred

    y_test

    import random

    data = []

    for i in range(1, 101):
        number = random.randint(0, 300)
        data.append(number)

    data

    result = classifier.predict([data])

    result

    if result == 1:
        print("This is malware")
    else:
        print("Benign")


def arbitrary():
    detect()

gui = Malware_Detection()
gui.root.mainloop()
