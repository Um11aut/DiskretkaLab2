import numpy as np

def task13():
    first = np.array(["A", "B", "C", "D", "E", "F", "G"])
    second = np.array(["D", "E", "F", "G", "M", "Y", "P"])
    sum = np.concatenate((first, second))
    print(np.unique(sum))
