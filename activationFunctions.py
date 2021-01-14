import numpy as np


def sigmoid(Z):
    # Sigmoid activation function
    # returns cache with Z and output A
    A = 1/(1+np.exp(-Z))

    assert(A.shape == Z.shape)

    cache = Z

    return A, cache


def relu(Z):
    # ReLU activation function

    A = np.maximum(0, Z)

    assert(A.shape == Z.shape)

    cache = Z
    return A, cache


def relu_backward(dA, Z):
    # backwards propogation for ReLU

    dZ = np.array(dA, copy=True)

    dZ[Z <= 0] = 0

    assert (dZ.shape == Z.shape)

    return dZ


def sigmoid_backward(dA, Z):
    # backwards propogation for sigmoid

    s = 1/(1+np.exp(-Z))
    dZ = dA*s*(1-s)

    assert(dZ.shape == Z.shape)

    return dZ
