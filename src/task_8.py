import numpy as np

def task8():
    arr = np.arange(1,101)
    print(np.array2string(arr, separator=', '))
    print(np.array2string(arr.reshape(100,1), separator=', '))

