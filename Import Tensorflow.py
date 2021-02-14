import tensorflow as tf


def my_func(arg):
    arg = tf.convert_to_tensor(arg, dtype=tf.float32)
    return arg


value_1 = my_func(tf.constant([[1.0, 2.0], [3.0, 4.0]]))
print(value_1)
