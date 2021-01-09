import pandas as pd
import numpy as np
# list of all the balanced datafiles that need to be read
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
unbalancedFiles = [
    "D:/Research PSU 2020/Clean Unbalanced MEMS/166_14Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/167_14Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/168_17Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/169_25Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/170_25Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/171_25Hz_10s.xlsx",
    "D:/Research PSU 2020/Clean Unbalanced MEMS/172_25Hz_10s.xlsx"]
# implement randomization here for all files
allFiles = balancedFiles + unbalancedFiles
m_train = 5
m_test = len(allFiles) - m_train
counter = 0
# initializing the training and testing set arrays and allocating their space
train_set_x_orig = np.zeros((8000, m_train))
train_set_y_orig = np.zeros((1, m_train))
test_set_x_orig = np.zeros((8000, m_test))
test_set_y_orig = np.zeros((1, m_test))
# split each file into frames to get more training examples

# for loop to organize flatten and put into the respective test and training sets
for i in allFiles:
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

# size of data read has to be 4000
# resizedarr = np.delete(arr, np.s_[5:], 0)
# print(resizedarr)
# arr_flatten = resizedarr.reshape(1, resizedarr.shape[0]*resizedarr.shape[1]).T
# for loop through each excel file
# create an array from each excel file and store in temp variable
# take this temporary array and flatten it by using the .shape
# append this as a new index to the final test or train set array
# append correct balanced(1) or unbalanced(0) value to y value array
# go back through loop
# finarr = arr_flatten
# finarr = np.append(finarr, arr_flatten, axis=1)
# print(finarr)
# need trainsetx,y and testsetx,y
# y will just be determined from folder of the read
# each example in training set will be the z and timestamp flattened together
# you can use dataframe.to_numpy() to turn into arrays
