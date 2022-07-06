import numpy as np
import sys

FILE_PATH = '../data/rtdl/N_train.npy'
np.set_printoptions(threshold=sys.maxsize)
data = np.load(FILE_PATH)
print(data)
print(data.shape)