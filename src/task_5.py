import random

def RandomArray(N: int):
    possible_values = list(range(1, N + 1))
    
    result_array = []
    
    while possible_values:
        random_index = random.randint(0, len(possible_values) - 1)
        
        result_array.append(possible_values.pop(random_index))
    
    return result_array

def task5():
    print(RandomArray(10))