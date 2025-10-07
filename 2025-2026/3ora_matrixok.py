import random
import math
import numpy as np
import matplotlib.pyplot as plt

mtx = [[4, 3, 1, 6, 4, 7, 3],
       [0, 3, 1, 6, 1, 3, 2],
       [7, 3, 1, 6, 4, 0, 3],
       [4, 3, 1, 6, 4, 1, 3],
       [9, 8, 1, 9, 4, 0, 3],]

print(mtx)
for row in mtx:
    print(row)
print(mtx[2][5])

# Programozási tételek mátrixokra:
# sor-oszlop vagy oszlop-sor bejárást alkalmazzuk

# Összegzés tétele:
osszeg = 0
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        osszeg += 1
print(osszeg)

# Eldöntés tétele (Van-e  9-es szám a mátrixban?) 

van_kilenc = False
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] == 9:
            van_kilenc = True
            break

# Maximum kiválasztás:

max = mtx[0][0]
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] > max:
            max = mtx[i][j]
print(max)

# Megszámlálás tétele: (számoljuk meg, hogy hány páratlan szám van a mátrixban)

paratlan = 0
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] % 2 == 1:
            paratlan += 1
print(paratlan)