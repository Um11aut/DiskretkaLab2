import numpy as np

def task7():
    matrix = np.arange(1.0, 101.0).reshape(10, 10)
    print(np.array2string(matrix, separator=', '))
