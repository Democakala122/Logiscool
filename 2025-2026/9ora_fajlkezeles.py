import os
import random

path_olimpia = os.path.dirname(__file__) # Az a mappa amiben a jelenleg futó script van
print(path_olimpia)
path_olimpia = os.path.join(path_olimpia, "forras", "olimpia.txt")
print(path_olimpia)

f = open(path_olimpia, "r", encoding="utf-8")
"""
szöveg = f.read(12)
for line in f:
    print(line.strip())


lines = f.readlines()
#print(lines)

f.close

f = open(path_olimpia, "r", encoding="utf-8")
szöveg = f.read
f.close()
"""
# Fájlkezelésnél ajánlott a context manager használata:

with open(path_olimpia, "r", encoding="utf-8"):
    print(f.read(20))

# with-en kívül, már nem lesz megnyitva a fájl

def generate_matrix(rows, cols):
    mtx = []
    for i in range(rows):
        lista = []
        for j in range(cols):
            lista.append(random.randint(0, 70))
        mtx.append(lista)
    return mtx

matrix = generate_matrix(38, 5)
print(matrix)
output_path = os.path.dirname(__file__)
output_path = os.path.join(output_path, "matrix.txt")

"""
with open(output_path, "w", encoding="utf-8") as f:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != len(matrix[i]) - 1:
                f.write(f"{matrix[i][j]}; ")
            else:
                f.write(f"{matrix[i][j]}")
    f.write("\n")
"""

# Olvassuk be és tároljuk el a "hőmérséklet.txt"-ben található adatokat

# Hozzunk letre egy homersek_elemzes.txt fájlt aminek tartalma:
# Az átlag hőmérséklet: x
# A leghidegebb hőmérséklet: x
# A leghidegebb nap az év x. napján volt 
# A heti szintű átlaghőmérséklet: [3, 7, 3, 6, 7, ...] (52 elem)
"""
finder = os.path.dirname(__file__)
finder = os.path.join(finder, "homerseklet.txt")

with open(finder, "r", encoding="utf-8") as f:
    matrix = []
    for line in f:
        lista = line.strip()
        lista = lista.split(";")
        matrix.append(lista)

finder = os.path.dirname(__file__)
finder = os.path.join(finder, "homerseklet_elemzes.txt")

def find_list_atlag(lista):
    atlag = 0
    for szam in lista:
        atlag += szam
    return atlag / len(lista)

def find_mtx_atlag(mtx):
    osszeg = 0
    div = 0
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            osszeg += mtx[i][j]
            div += 1
    return osszeg / div

def find_cold_day(mtx):
    low = mtx[0][0]
    div = 0
    retdiv = 0
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            div += 1
            if mtx[i][j] < low:
                low = mtx[i][j]
                retdiv = div
    return (low, retdiv)

with open(finder, "w", encoding="utf-8") as f:
    f.write(f"Az átlag hőmérséklet: {find_mtx_atlag(matrix)}")
    f.write(f"A leghidegebb hőmérséklet: {find_cold_day(matrix)[0]}")
    f.write(f"A leghidegebb nap az év {find_cold_day(matrix)[1]}. napján volt")
"""

#TODO Befejzni ezt a cuccot mert tudom hogy megtudom csinálni, de nincs kedv
#     Átírni mert forrás mappa
