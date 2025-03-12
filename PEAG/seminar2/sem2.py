import random as rand
import numpy as np
import matplotlib.pyplot as grafic

def fitness(v, c, cm, x):
    valoare = np.dot(v, x)
    cost  = np.dot(c, x)
    return valoare, cost <= cm

def generare(fis_v, fis_c, cm, dimensiune):
    v = np.genfromtxt(fis_v)
    c = np.genfromtxt(fis_c)
    n = len(v)
    populatie = []
    i = 0
    while i < dimensiune:
        x = rand.choices([0, 1], k=n)
        val, fezabil = fitness(v, c, cm, x)
        if fezabil:
            x.append(val)
            populatie.append(x)
            i += 1
    deseneaza(populatie, dimensiune)
    return populatie

def deseneaza(populatie, dim):
    OX = [i for i in range(dim)]
    OY = [populatie[i][-1] for i in range(dim)]
    grafic.plot(OX, OY, "ro", markersize=10)
    grafic.show()

if __name__ == "__main__":
    P = generare("valoare.txt", "cost.txt", 45, 10)
    for element in P:
        print(f"Individul {element[:-1]} cu fitness {element[-1]}")
