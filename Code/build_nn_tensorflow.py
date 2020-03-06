import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint,Callback
from tensorflow.keras import optimizers,losses,activations,initializers

from tensorflow.keras.layers import Dense,Dropout,Activation

from tensorflow.keras.callbacks import ModelCheckpoint,Callback

from sklearn.preprocessing import StandardScaler

# get the date
train = pd.read_csv('alle_Versuch_merge_processing_sortet.CSV')
# train.shape  = (1016988, 26)


# define X and y
X = train[['Size Area (um2)', 'Actual_Druck(Kg)', 'Actual Temperature (oC)',
       'Actual Humidity (%)', 'Print Speed (mm/sec)',
       'Separation Speed (mm/s)']].values
y = train[['Volume (%)','Area (%)']].values

# now begin to train a neural network

# hyperparameter setting
validation_split=0.25

initializers = ['normal', 'he_uniform']
#activations = ['tanh','exponential','softplus','softsign']
activations = ['relu','sigmoid','softmax']
#losses = ['mse','categorical_crossentropy','hinge','mean_absolute_error','poisson']
losses = ['mse','categorical_crossentropy','mean_absolute_error']
optimizers = ['adam','sgd']

# tuning and print the result for each hyperparameter combination
model = Sequential()
for init in initializers:
    for acti in activations:
        for loss in losses: 
            for opti in optimizers:
                model.add(Dense(128,kernel_initializer=init,input_dim=6,activation=acti))
                    
                model.add(Dense(256, kernel_initializer=init,activation=acti))
                model.add(Dense(256, kernel_initializer=init,activation=acti))
                model.add(Dense(256, kernel_initializer=init,activation=acti))
                model.add(Dense(256, kernel_initializer=init,activation=acti))
                    
                model.add(Dense(2,kernel_initializer=init,activation=acti))
                    
                model.compile(loss=loss, optimizer = opti, metrics=['accuracy'])
                    
                    
                checkpoint_name = 'Weights-{}-{}-{}-{}---.hdf5'.format(init,acti,loss,opti) 
                checkpoint = ModelCheckpoint(checkpoint_name, monitor='val_loss', verbose = 1, save_best_only = True, mode ='auto')
                callbacks_list = [checkpoint]
                    
                model.summary()
                model.fit(X, y, epochs=10, batch_size=1024, validation_split = validation_split,callbacks=callbacks_list)
