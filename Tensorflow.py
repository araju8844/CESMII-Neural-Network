import importTF
from dataSetCreator import *
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# getting data from randomized set
x_train, y_train, x_test, y_test = createDataSet()
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

# turning the numpy arrays into normalized tensors
x_train = importTF.my_func(x_train)
x_test = importTF.my_func(x_test)
y_train = importTF.my_func(y_train)
y_test = importTF.my_func(y_test)
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# TODO: Normalize the vectors and put them into new train and test sets

# Labels: Balanced and Unbalanced Outputs
model = tf.keras.models.Sequential()
# do i need the flatten here i dont know how to do it otherwise
model.add(keras.layers.Flatten())
model.add(tf.keras.layers.BatchNormalization())
model.add(keras.layers.Dense(3, activation="relu"))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(.1))
model.add(keras.layers.Dense(5, activation="relu"))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(.1))
#model.add(keras.layers.Dense(2, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

model.compile(optimizer='adam',
              loss='binary_crossentropy', metrics=['accuracy'])
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
callbacks = []
model.fit(x_train, y_train, batch_size=50, epochs=16)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

# saving and loading model
'''
model.save('namehere')
new_model = tf.keras.models.load_model)
'''
