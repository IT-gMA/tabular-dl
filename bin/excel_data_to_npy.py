import numpy as np
import pandas as pd
import os
import sys

EXCEL_DATA = '../BLEVE_data/BLEVE_data_shuffled.xlsx'  # Given this data has been randomised beforehand
SAVE_DIR = '../data/bleve'


def read_and_convert():
    np.set_printoptions(threshold=sys.maxsize)
    df = pd.read_excel(EXCEL_DATA)

    np_arr = df.to_numpy(dtype=np.float32)
    row, col = np_arr.shape
    features_arr = np.empty(shape=(row, col - 1), dtype=np.float32)  # Exclude the output column from this data
    outputs_arr = np.empty(shape=(row,), dtype=np.float32)  # This numpy array represent the output column

    i = 0
    for i in range(row):
        # Separate the last column (output) from the rest of the cell
        outputs_arr[i] = np_arr[i][-1]

    # Extract the first n-1 columns
    features_arr = np.delete(np_arr, -1, axis=1)

    return features_arr, outputs_arr


def training_split(features, outputs, ratio=(0.70, 0.15, 0.15)):
    num_samples = outputs.shape[0]
    num_train = int(num_samples * ratio[0])
    num_val = int(num_samples * ratio[1])
    num_test = num_samples - num_train - num_val

    N_train = features[0:num_train]
    N_val = features[num_train:(num_val + num_train)]
    N_test = features[(num_val + num_train):]

    y_train = outputs[0:num_train]
    y_val = outputs[num_train:(num_val + num_train)]
    y_test = outputs[(num_val + num_train):]

    return N_train, N_val, N_test, y_train, y_val, y_test


def save_npy(N_train, N_val, N_test, y_train, y_val, y_test):
    np.save(file=f'{SAVE_DIR}/N_train.npy', arr=N_train)
    np.save(file=f'{SAVE_DIR}/N_val.npy', arr=N_val)
    np.save(file=f'{SAVE_DIR}/N_test.npy', arr=N_test)
    np.save(file=f'{SAVE_DIR}/y_train.npy', arr=y_train)
    np.save(file=f'{SAVE_DIR}/y_val.npy', arr=y_val)
    np.save(file=f'{SAVE_DIR}/y_test.npy', arr=y_test)


if __name__ == '__main__':
    features, outputs = read_and_convert()

    # 70% used for training, 15% for validation and 15% for testing
    num_train = 0.70
    num_val = 0.1503
    num_test = 0.1497
    ratio = (num_train, num_val, num_test)
    N_train, N_val, N_test, y_train, y_val, y_test = training_split(features, outputs, ratio)
    print("train {}:{}\nvalidation {}:{}\ntest {}:{}".format(num_train * 100, len(N_train), num_val * 100, len(N_val),
                                                             num_test * 100, len(N_test)))

    # Save the samples as .npy files
    save_npy(N_train, N_val, N_test, y_train, y_val, y_test)
