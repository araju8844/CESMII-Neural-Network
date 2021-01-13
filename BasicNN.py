import pandas as pd
import numpy as np
from dataOrganizer import initNumpyDict
from random import sample
# list of all the balanced datafiles that need to be read
# ADD the balanced excel files here here
balancedFiles = [
    "D:/Research PSU 2020/Clean Balanced MEMS/151_10Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Balanced MEMS/152_10Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Balanced MEMS/153_12Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Balanced MEMS/154_15Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Balanced MEMS/155_17Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Balanced MEMS/156_25Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Balanced MEMS/157_25Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Balanced MEMS/158_10Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Balanced MEMS/159_17Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Balanced MEMS/160_25Hz_10s.xlsx"]
# lift of all the unbalanced files
# ADD the unbalanced excel files here
unbalancedFiles = [
    "D:/Research PSU 2020/Clean Unbalanced MEMS/166_14Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/167_14Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/168_17Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/169_25Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/170_25Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/171_25Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/172_25Hz_10s.xlsx"]

# length of each frame for each training example
frameLength = 60
allFiles = balancedFiles + unbalancedFiles
# empty dictionary to put the necessary data in with the function
numpyDict = {}
m = initNumpyDict(frameLength, numpyDict, allFiles, balancedFiles)
# TODO: edit m_train and frameLength
# initialize a numpy array that has the space to contain all the training examples
# array has frameLength*2 when flattened
allExamples = np.zeros((frameLength*2, m))
# create the training examples at each frame length and put in allExamples
# create an array that has the values from 0 to m arranged in a random array
randomizedIndex = sample(list(range(0, m)), m)
i = 0
# iterate through each sheet
for sheet in allFiles:
    j = 0
    # creates the dataset and assigns to random position
    while j + frameLength < numpyDict[sheet][0].shape[0]:
        allExamples[:, randomizedIndex[i]] = numpyDict[sheet][0][j:j +
                                                                 frameLength].reshape(2*frameLength)
        # increment j by 30 and the examples index by 1
        j += frameLength//2
        i += 1

print(allExamples.shape)


m_train = 4
m_test = len(allFiles) - m_train


# initializing the training and testing set arrays and allocating their space
train_set_x_orig = np.zeros((8000, m_train))
train_set_y_orig = np.zeros((1, m_train))
test_set_x_orig = np.zeros((8000, m_test))
test_set_y_orig = np.zeros((1, m_test))

# for loop to create each training example will randomize separately
"""for i in allFiles:
    #read the excel file
    fileDataframe = pd.read_excel(i)
    #convert to numpy array
    fileData = fileDataframe.to_numpy()
    j = 0
    #while loop to create each training example
    while j+60 < fileData.shape[1]:
        
        #increment by 30
        j+= 30    
"""
"""for i in allFiles:
    # read the file
    dataframe = pd.read_excel(i)
    # convert to numpy
    temparr = dataframe.to_numpy()
    # giving all data a common size by making it shape (4000,2)
    temparr = np.delete(temparr, np.s_[4000:], 0)
    print(temparr.shape)
    # flattening by training example
    arr_flatten = temparr.reshape(1, temparr.shape[0]*temparr.shape[1])
    # puts it into training or testing set depending on allocated m_train
    if counter < m_train:
        # putting this into the necessary column
        train_set_x_orig[:, counter] = arr_flatten
        # if i is from the balanced dataset gives 1 else gives a 0
        train_set_y_orig[counter] = i in balancedFiles
    else:
        # putting this into the necessary column
        train_set_x_orig[:, counter - m_train] = arr_flatten
        # if i is from the balanced dataset gives 1 else gives a 0
        train_set_y_orig[counter - m_train] = i in balancedFiles
    counter += 1
"""
# append correct balanced(1) or unbalanced(0) value to y value array
# you can use dataframe.to_numpy() to turn into arrays
