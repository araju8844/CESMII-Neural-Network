from dataSetCreator import *
import numpy as np
import tensorflow as tf

# getting data from randomized set
x_train, y_train, x_test, y_test = createDataSet()
print(x_train.shape, y_train.shape, x_test.shape)

# turning the numpy arrays into normalized tensors
x_train = tf.keras.utils.normalize(tf.convert_to_tensor(x_train), axis=1)
x_test = tf.keras.utils.normalize(tf.convert_to_tensor(x_test), axis=1)
y_train = tf.convert_to_tensor(y_train)
y_test = tf.convert_to_tensor(y_test)

model = tf.keras.models.Sequential()
# do i need the flatten here i dont know how to do it otherwise
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(30, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(20, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(1, activation=tf.nn.sigmoid))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=100, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

# saving and loading model
'''
model.save('namehere')
new_model = tf.keras.models.load_model)
'''
