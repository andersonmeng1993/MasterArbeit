'''
https://www.tensorflow.org/tutorials/keras/save_and_load#hdf5_format

# Recreate the exact same model, including its weights and the optimizer
new_model = tf.keras.models.load_model('my_model.h5')

# Show the model architecture
new_model.summary()

# check its accuracy
loss, acc = new_model.evaluate(test_images,  test_labels, verbose=2)
print('Restored model, accuracy: {:5.2f}%'.format(100*acc))

'''

import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# test whether it will run with tensorflow-gpu
# tf.test.is_gpu_available
tf.test.gpu_device_name()

# read a trained model
model_1 = tf.keras.models.load_model('Weights-normal-sigmoid-categorical_crossentropy-adam---.hdf5')
# show detail of a saved model
model_1.summary()

# read the test date
testset_1 = pd.read_csv('Testset_von_FCT/testset_1.CSV')
testset_2 = pd.read_csv('Testset_von_FCT/testset_2.CSV')
testset_3 = pd.read_csv('Testset_von_FCT/testset_3.CSV')

# set input respectively for different test date
testset_1_input = testset_1[['Size Area (um2)','Actual_Druck(Kg)','Actual Temperature (oC)', 'Actual Humidity (%)','Actual Separation Speed (mm/s)', 'Rear Print Speed (mm/sec)']]
testset_2_input = testset_2[['Size Area (um2)','Actual_Druck(Kg)','Actual Temperature (oC)', 'Actual Humidity (%)','Actual Separation Speed (mm/s)', 'Rear Print Speed (mm/sec)']]
testset_3_input = testset_3[['Size Area (um2)','Actual_Druck(Kg)','Actual Temperature (oC)', 'Actual Humidity (%)','Actual Separation Speed (mm/s)', 'Rear Print Speed (mm/sec)']]

# set output
testset_1_output = testset_1[['Volume (%)', 'Area (%)']]
testset_2_output = testset_2[['Volume (%)', 'Area (%)']]
testset_3_output = testset_3[['Volume (%)', 'Area (%)']]

# now evaluate the model with 3 test datesets
print('\n# Evaluate, Dataset 1')
model_1.evaluate(x=testset_1_input,y=testset_1_output,batch_size=256)

print('\n# Evaluate, Dataset 2')
model_1.evaluate(x=testset_2_input,y=testset_2_output,batch_size=256)

print('\n# Evaluate, Dataset 3')
model_1.evaluate(x=testset_3_input,y=testset_3_output,batch_size=256)
