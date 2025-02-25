import sys

lista = [11, -4, 7, 1, 6, -5, -12, 0, 11, 14, -8, -9, 2, 23, 11, 10, -4, 0, 18, 4, 8, 1, 1, 11]
var = 0

#1 feladat: Határozzuk meg a lista eleminek az összegét
for item in lista:
    var += item
print("A lista elemeinek az összege:", var)

#2 feladat: Határozzuk meg a pozitív számok összegét
var = 0
for item in lista:
    if item > 0:
        var += item
print("A lista pozitív számainak összege:", var)

#3 feladat: Melyik a legnagyobb szám?
var = -sys.maxsize
for item in lista:
    if item > var:
        var = item
print("a legnagyobb szám:", var)

#4 feladat: Melyik a legkisebb szám?
var = sys.maxsize
for item in lista:
    if item < var:
        var = item
print("a legkisebb szám:", var)

#5 feladat: Hány darab 10-nél nagyobb szám van a listában?
var = 0
for item in lista:
    if item > 10:
        var += 1
print("Ennyi 10-nél nagyobb szám van:", var)

#6 feladat: Határozzuk meg a lista eleminek az átlagát
var = 0
for item in lista:
    var += item
var = round(var / len(lista), 2)
print("a lista eleminek az átlaga:", var)

#7 feladat: Válogassuk szét a lista elemeit két másik listára: pozitív, negatív
poz = []
neg = []
for item in lista: # Ha az item 0 nulla egyik listába se kerül, de a feladat szerint 2 csoportba osszuk, szóval azt csináltam
    if item > 0:
        poz.append(item)
    elif item < 0:
        neg.append(item)
print("Pozitív számok: ", poz, "Negatív számok: ", neg)