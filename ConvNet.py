import numpy as np
from matplotlib import pyplot as plt
from dataSetCreator import *
from scipy.fft import fft, fftfreq
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import importTF

x_train, y_train, x_test, y_test, = piezoDataset()
x_train = x_train.reshape(-1, 32, 32, 1)
x_test = x_test.reshape(-1, 32, 32, 1)
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

model = tf.keras.Sequential()

model.add(layers.Conv2D(filters=6, kernel_size=(3, 3),
                        activation='relu', input_shape=(32, 32, 1)))
model.add(layers.AveragePooling2D())

model.add(layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
model.add(layers.AveragePooling2D())

model.add(layers.Flatten())

model.add(layers.Dense(units=120, activation='relu'))

model.add(layers.Dense(units=84, activation='relu'))

model.add(layers.Dense(units=1, activation='sigmoid'))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
              loss='binary_crossentropy', metrics=['accuracy'])
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
callbacks = []
model.fit(x_train, y_train, batch_size=50, epochs=32)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)
