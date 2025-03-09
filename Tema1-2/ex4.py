import numpy as np

def insertSort(vector):
    for i in range(1, len(vector)):
        key = vector[i]
        j = i-1
        while j >= 0 and key < vector[j]:
            vector[j+1] = vector[j]
            j -= 1
        vector[j+1] = key
    return vector

m = np.array([[3, 1, 2], [3, 2, 4], [3, 3, 5], [6, 6, 0]])
vec = np.array([9, 4, 6, 1, 7, 3, 8, 5, 2, 10])

for vector in m:
    insertSort(vector)

insertSort(vec)

print(m)
print(vec)