import numpy as np;

def calcNoOfLines(vector):
    result = 0
    for array in m:
        flag = True
        for i in range(len(array) - 1):
            if array[i + 1] < array[i]:
                flag = False
        if flag:
            result += 1
    return result

m = np.array([[2, 3], [3, 4], [3, 3], [2, 0]])

print(calcNoOfLines(m))