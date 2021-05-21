import numpy as np
from matplotlib import pyplot as plt
from dataSetCreator import *
from scipy.fft import fft, fftfreq
x_train, time_train, y_train, x_test, y_test, time_test = fftDataset()
yf = fft(x_train)
xf = fftfreq()
plt.plot(time_train[0], x_train[0])
plt.show()
