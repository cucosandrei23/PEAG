import random
import numpy as np

def calcVect(matr):
    vector = np.zeros(20)
    for i in range(20):
        s = 0
        for j in range(7):
            s += matr[i][j]
        vector[i] = s
    return vector

def orderVect(matr, vec):
    for i in range(1, len(vec)):
        key = vec[i]
        key_m = matr[i]
        j = i - 1
        while j >= 0 and vec[j] > key:
            vec[j+1] = vec[j]
            matr[j+1] = matr[j]
            j -= 1
        vec[j+1] = key
        matr[j+1] = key_m

    return matr, vec

a = np.zeros((20, 7))
for i in range(20):
    for j in range(7):
        a[i][j] = random.randint(0, 1)
v = calcVect(a)
print(a)
print(v)
print(orderVect(a, v))



