import pandas as pd
import numpy as np
from dataOrganizer import initNumpyDict, initNumpyDictPiezo
from random import sample
# list of all the balanced datafiles that need to be read
# ADD the balanced excel files here here
'''balancedFiles = [
    "Clean Balanced MEMS/151_10Hz_10s.xlsx",
    "Clean Balanced MEMS/152_10Hz_10s.xlsx",
    "Clean Balanced MEMS/153_12Hz_10s.xlsx",
    "Clean Balanced MEMS/154_15Hz_10s.xlsx",
    "Clean Balanced MEMS/155_17Hz_10s.xlsx",
    "Clean Balanced MEMS/156_25Hz_10s.xlsx",
    "Clean Balanced MEMS/157_25Hz_10s.xlsx",
    "Clean Balanced MEMS/158_10Hz_10s.xlsx",
    "Clean Balanced MEMS/159_17Hz_10s.xlsx",
    "Clean Balanced MEMS/160_25Hz_10s.xlsx"]
# lift of all the unbalanced files
# ADD the unbalanced excel files here
unbalancedFiles = [
    "Clean Unbalanced MEMS/166_14Hz_10s.xlsx",
    "Clean Unbalanced MEMS/167_14Hz_10s.xlsx",
    "Clean Unbalanced MEMS/168_17Hz_10s.xlsx",
    "Clean Unbalanced MEMS/169_25Hz_10s.xlsx",
    "Clean Unbalanced MEMS/170_25Hz_10s.xlsx",
    "Clean Unbalanced MEMS/171_25Hz_10s.xlsx",
    "Clean Unbalanced MEMS/172_25Hz_10s.xlsx"]'''

# ADD the balanced excel files here here
balancedFiles = [
    "Shaft_vibration_data-Ankur_Verma/Balanced_shaft_Piezo/vib_mfs_10hz.xlsx",
    "Shaft_vibration_data-Ankur_Verma/Balanced_shaft_Piezo/vib_mfs_12hz.xlsx",
    "Shaft_vibration_data-Ankur_Verma/Balanced_shaft_Piezo/vib_mfs_15hz.xlsx",
    "Shaft_vibration_data-Ankur_Verma/Balanced_shaft_Piezo/vib_mfs_17hz.xlsx",
    "Shaft_vibration_data-Ankur_Verma/Balanced_shaft_Piezo/vib_mfs_25hz.xlsx",
    "Shaft_vibration_data-Ankur_Verma/Balanced_shaft_Piezo/vib_mfs2_10hz.xlsx",
    "Shaft_vibration_data-Ankur_Verma/Balanced_shaft_Piezo/vib_mfs2_17hz.xlsx",
    "Shaft_vibration_data-Ankur_Verma/Balanced_shaft_Piezo/vib_mfs2_25hz.xlsx"]
# lift of all the unbalanced files
# ADD the unbalanced excel files here
unbalancedFiles = [
    "Shaft_vibration_data-Ankur_Verma/Unbalanced_shaft_Piezo/vib_mfsu_14hz.xlsx",
    "Shaft_vibration_data-Ankur_Verma/Unbalanced_shaft_Piezo/vib_mfsu_17hz.xlsx",
    "Shaft_vibration_data-Ankur_Verma/Unbalanced_shaft_Piezo/vib_mfsu_25hz.xlsx"]
# CHANGE FRAME LENGTH AND TRAIN/TEST RATIO HERE
# length of each frame for each training example
frameLength = 32*32
trainRatio = .80


allFiles = balancedFiles + unbalancedFiles


def createDataSet():
    # empty dictionary to put the necessary data in with the function
    numpyDict = {}
    m = initNumpyDict(frameLength, numpyDict, allFiles, balancedFiles)
    print(numpyDict)
    # TODO: edit m_train and frameLength
    # initialize a numpy array that has the space to contain all the training examples
    # array has frameLength*2 when flattened
    allExamples = np.zeros((frameLength*2, m))
    allOutcomes = np.zeros((1, m))

    # create the training examples at each frame length and put in allExamples
    # create an array that has the values from 0 to m arranged in a random array
    randomizedIndex = sample(list(range(0, m)), m)
    i = 0
    # iterate through each sheet
    for sheet in allFiles:
        j = 0
        # creates the dataset and assigns to random position
        while j + frameLength < numpyDict[sheet][0].shape[0]:
            # print("enter")
            allExamples[:, randomizedIndex[i]] = numpyDict[sheet][0][j:j +
                                                                     frameLength].reshape(2*frameLength)
            # print("exit")
            # Balanced with 1 unbalanced with 0
            allOutcomes[0, randomizedIndex[i]] = sheet in balancedFiles
            # increment j by 30 and the examples index by 1
            j += frameLength//2
            i += 1

    # initialize m_train and test
    m_train = int(m*trainRatio)
    m_test = m - m_train
    # initializing the training and testing set arrays and allocating their space
    train_set_x_orig = np.transpose(allExamples[:, 0:m_train])
    train_set_y_orig = np.transpose(allOutcomes[:, 0:m_train])
    test_set_x_orig = np.transpose(allExamples[:, m_train:])
    test_set_y_orig = np.transpose(allOutcomes[:, m_train:])

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig


def lenetDataset():
    # empty dictionary to put the necessary data in with the function
    numpyDict = {}
    m = initNumpyDict(frameLength, numpyDict, allFiles, balancedFiles)
    # TODO: edit m_train and frameLength
    # initialize a numpy array that has the space to contain all the training examples
    # array has frameLength*2 when flattened
    allWaves = np.zeros((32, 32, m))
    #allTimes = np.zeros((frameLength, m))
    allOutcomes = np.zeros((1, m))
    # temp wave so we can do frame overlap sideways
    prevWave = np.zeros((32, 16))
    # create the training examples at each frame length and put in allExamples
    # create an array that has the values from 0 to m arranged in a random array
    randomizedIndex = sample(list(range(0, m)), m)
    i = 0
    # iterate through each sheet
    for sheet in allFiles:
        j = 0
        # creates the dataset and assigns to random position
        transposeTst = np.transpose(numpyDict[sheet][0])
        while j + frameLength < numpyDict[sheet][0].shape[0]:
            # print("enter")
            #[0] is wave [1] is time
            allWaves[:, :, randomizedIndex[i]
                     ] = transposeTst[0][j:j+frameLength].reshape(32, 32)
            # allTimes[:, randomizedIndex[i]
            # ] = transposeTst[1][j:j+frameLength]
            # print("exit")
            # Balanced with 1 unbalanced with 0
            allOutcomes[0, randomizedIndex[i]] = sheet in balancedFiles
            # increment j by 30 and the examples index by 1
            j += frameLength//2
            i += 1

    # initialize m_train and test
    m_train = int(m*trainRatio)
    m_test = m - m_train
    # initializing the training and testing set arrays and allocating their space
    train_set_x_orig = np.transpose(allWaves[:, :, 0:m_train])
    train_set_y_orig = np.transpose(allOutcomes[:, 0:m_train])
    test_set_x_orig = np.transpose(allWaves[:, :, m_train:])
    test_set_y_orig = np.transpose(allOutcomes[:, m_train:])

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig


def piezoDataset():
    # empty dictionary to put the necessary data in with the function
    numpyDict = {}
    m = initNumpyDictPiezo(frameLength, numpyDict, allFiles, balancedFiles)
    # TODO: edit m_train and frameLength
    # initialize a numpy array that has the space to contain all the training examples
    # array has frameLength*2 when flattened
    allWaves = np.zeros((32, 32, m))
    #allTimes = np.zeros((frameLength, m))
    allOutcomes = np.zeros((1, m))
    # temp wave so we can do frame overlap sideways
    prevWave = np.zeros((32, 16))
    # create the training examples at each frame length and put in allExamples
    # create an array that has the values from 0 to m arranged in a random array
    randomizedIndex = sample(list(range(0, m)), m)
    i = 0
    # iterate through each sheet
    for sheet in allFiles:
        j = 10
        # creates the dataset and assigns to random position
        transposeTst = np.transpose(numpyDict[sheet][0])
        while j + frameLength < numpyDict[sheet][0].shape[0]:
            # print("enter")
            #[0] is wave [1] is time
            allWaves[:, :, randomizedIndex[i]
                     ] = transposeTst[1][j:j+frameLength].reshape(32, 32)
            # allTimes[:, randomizedIndex[i]
            # ] = transposeTst[1][j:j+frameLength]
            # print("exit")
            # Balanced with 1 unbalanced with 0
            allOutcomes[0, randomizedIndex[i]] = sheet in balancedFiles
            # increment j by 30 and the examples index by 1
            j += frameLength//2
            i += 1

    # initialize m_train and test
    m_train = int(m*trainRatio)
    m_test = m - m_train
    # initializing the training and testing set arrays and allocating their space
    train_set_x_orig = np.transpose(allWaves[:, :, 0:m_train])
    train_set_y_orig = np.transpose(allOutcomes[:, 0:m_train])
    test_set_x_orig = np.transpose(allWaves[:, :, m_train:])
    test_set_y_orig = np.transpose(allOutcomes[:, m_train:])

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig
