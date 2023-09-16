import numpy as np

def re(arr: np.array):
    res = []
    for el in arr:
        if el % 3 == 0:
            res.append(el)
    return res


def task12():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 9, 11, 12])
    result = re(arr)
    print(result)