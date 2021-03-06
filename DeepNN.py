import time
import numpy as np
import matplotlib.pyplot as plt
import scipy
from DeepNNHelpers import *
from dataSetCreator import *

# create the dataset with randomized testing and training sets
# NOTE: edit the files in dataSetCreator to edit the data within the dataset
train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig = createDataSet()

print(train_set_x_orig.shape, train_set_y_orig.shape,
      test_set_y_orig.shape, test_set_x_orig.shape)

### CONSTANTS ###
layers_dims = [train_set_x_orig.shape[0], 3, 1]


def L_layer_model(X, Y, layers_dims, learning_rate=0.0075, num_iterations=3000, print_cost=False):  # lr was 0.009
    """
Implements a L-layer neural network: [LINEAR -> RELU]*(L-1) -> LINEAR -> SIGMOID.

Arguments:
    X - - data, numpy array of shape(num_px * num_px * 3, number of examples)
    Y - - true "label" vector(containing 0 if cat, 1 if non-cat), of shape(1, number of examples)
    layers_dims - - list containing the input size and each layer size, of length(number of layers + 1).
    learning_rate - - learning rate of the gradient descent update rule
    num_iterations - - number of iterations of the optimization loop
    print_cost - - if True, it prints the cost every 100 steps

    Returns:
    parameters - - parameters learnt by the model. They can then be used to predict.
    """

    costs = []                         # keep track of cost

    # Parameters initialization. (≈ 1 line of code)
    parameters = initialize_parameters_deep(layers_dims)

    # Loop (gradient descent)
    for i in range(0, num_iterations):

        # Forward propagation: [LINEAR -> RELU]*(L-1) -> LINEAR -> SIGMOID.
        AL, caches = L_model_forward(X, parameters)

        # Compute cost.
        cost = compute_cost(AL, Y)

        # Backward propagation.
        grads = L_model_backward(AL, Y, caches)

        # Update parameters.
        parameters = update_parameters(parameters, grads, learning_rate)

        # Print the cost every 100 training example
        if print_cost and i % 100 == 0:
            print("Cost after iteration %i: %f" % (i, cost))
        if print_cost and i % 100 == 0:
            costs.append(cost)

    # plot the cost
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per hundreds)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()

    return parameters


parameters = L_layer_model(train_set_x_orig, train_set_y_orig,
                           layers_dims, num_iterations=2500, print_cost=True)
