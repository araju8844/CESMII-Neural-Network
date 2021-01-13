import pandas as pd
import numpy as np

"""Creates a dictionary with the file of origin as the key
and the respective data with balanced or unbalanced value as value"""


def initNumpyDict(frameLength, numpyDict, allFiles, balancedFiles):
    # m will be total training examples
    m = 0
    # iterate through all the files creating a new key and value for each Dictionary value
    for sheet in allFiles:
        numpyDict[sheet] = [pd.read_excel(
            sheet).to_numpy(), sheet in balancedFiles]
        # adding to m the total datapoints in the file divided by half a frameLength then - 1 to get available frames in that file
        m += int(((numpyDict[sheet][0].shape[0])//(frameLength/2)) - 1)
    return m
