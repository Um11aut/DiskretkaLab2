def task4_1(arr1: [], arr2: []):
    merged = []
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    merged = arr1 + arr2
    return sorted(merged)

def task4_2(arr1: [], arr2: []):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    return sorted(arr1 + arr2)

def task4():
    print(task4_1([1,2,3,4,5,7,8], [2,3,4,5,7,8,9,0,123,4324,2345543]))