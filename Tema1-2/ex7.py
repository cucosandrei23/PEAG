import numpy
import numpy as np

def transpus(matr):
    for i in range(len(matr)):
        for j in range(len(matr)):
            matr[i][j], matr[j][i] = matr[j][i], matr[i][j]
    return matr

def suma(matr1, matr2):
    for i in range(len(matr1)):
        for j in range(len(matr1)):
            matr1[i][j] += matr2[i][j]
    return matr1

def multiply(matr1, matr2):
    new = np.zeros((len(matr1), len(matr1[0])))
    for i in range(len(matr1)):
        for j in range(len(matr1)):
            s = 0
            for k in range(len(matr1)):
                s += (matr1[i][k] * matr2[k][j])
            new[i][j] = s
    return new

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(transpus(m))
print(suma(m, m))
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(multiply(m, m))