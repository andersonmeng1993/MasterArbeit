import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import svm,preprocessing,metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier,MLPRegressor



train = pd.read_csv('data_merged.CSV')

X = train[['Size Area (um2)', 'Actual_Druck(Kg)', 'Actual Temperature (oC)',
       'Actual Humidity (%)', 'Rear Print Speed (mm/sec)',
       'Actual Separation Speed (mm/s)']].values
y = train[['Volume (%)','Area (%)']].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

activations = ['logistic','relu']
solvers = ['sgd','adam']
alphas = [0.0001,0.001,0.01,0.1,1,10,50,100]
layers = [4,6,8]

for activation in activations:
    for solver in solvers:
        for alpha in alphas:
            for layer in layers:
                clf = MLPRegressor(hidden_layer_sizes=layer,activation=activation,solver=solver,alpha=alpha).fit(X_train,y_train)
                print("With activation '{}', solver '{}', alpha '{}' and hidden layer={}, the score of NN is {}".format(activation,solver,alpha,layer,clf.score(X_test,y_test)))
