import numpy as np

def bubbleSort(vector):

    for i in range(len(vector) - 1):
        maxim = 0
        for j in range(1, len(vector) - i):
            if vector[maxim] < vector[j]:
                maxim = j
        aux = vector[maxim]
        vector[maxim] = vector[-i-1]
        vector[-i-1] = aux
    return vector

m = np.array([[3, 2, 1], [3, 2, 4], [3, 3, 5], [6, 6, 0]])

for vector in m:
    bubbleSort(vector)

print(m)