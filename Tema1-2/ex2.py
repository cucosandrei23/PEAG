import numpy as np

def returnColumnIndex(matrix):
    result = []
    for i in range(len(matrix[0])):
        min = matrix[0][i]
        for j in range(len(matrix) - 1):
             if matrix[j + 1][i] < min:
                 min = matrix[j + 1][i]
        if min == 5:
            result.append(i+1)
    return result

m = np.array([[2, 5], [3, 6], [3, 7], [2, 8], [5, 9]])
print(returnColumnIndex(m))