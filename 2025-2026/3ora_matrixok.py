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

# List comperhension
lista = [i**2 for i in range(1, 11)]
print(lista) # 1, 4, 9, 16, 25 stb

mtx = [[i, i**2, i**3] for i in range(7)]
print(mtx)

mtx3d = [[[k for k in range(7)] for j in range(3)] for i in range(5)]
print(mtx3d)
összeg = 0

for i in range(len(mtx3d)):
    for j in range(len(mtx3d[i])):
        for k in range(len(mtx3d[i][j])):
            összeg += mtx3d[i][j][k]


# Kockák ábrázolása mathplotlibbel és numpy-al 

axes = [5,5,5]
cube = np.ones(axes) #Létrehoz egy 5*5*5 mátrixot tele 1-esekkel
colors = np.empty(axes + [3]) # Létrehoz egy 5*5*5*3-as mátrixot, üres értékekkel #csak lefoglalja a helyet a memóriában
# axes + [3] -> [5,5,5,3]
# print(colors) # Printelésnél azt látod, ami az előt volt azon a memória helyen
colors[0] = [1, 0, 0] # Piros
colors[1] = [0, 1, 0] # Zöld
colors[2] = [0, 0, 1] # Kék
colors[3] = [0, 1, 1] # Türkiz
colors[4] = [1, 1, 0] # Sárga

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.voxels(cube, facecolors=colors)

plt.show()

ter = np.ones([8,8,8])
colors = np.empty([8,8,8,3])
colors[:] = [0,0,1]