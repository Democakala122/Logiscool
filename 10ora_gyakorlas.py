import random
import math

#1 feladat: szedjük ki a duplikációkat a listából
szamok = [4, 1, 3, 9, 2, 8, 1, 8, 2, 4, 6, 3, 1, 0, 2, 5, 3, 2]

seen = []
i = 0
for szam in szamok:
    if szam not in seen:
        seen.append(szam)
print(seen)

# másik megoldás 
# set-ben minden elem csak egyszer szerepelhet
no_duplications = list(set(szamok))
print(no_duplications)

# extend függvény
lista1 = [6,3,2,9,2,18,1]
lista2 = [8,4,2,0,2,6,8,8]
lista3 = [1,2,3,4,5,6]

lista1.append(lista2)
print(lista1)

lista1.extend(lista3)
print(lista1)
sajt = True


# Válogassuk ki az int típusú objektumokat egy listából (egész számok)
lista = [4, 4.12, True, False, "cica", 5, 7, [1,2,3], 9, 4,2321, 0]
int_list = []
for item in lista:
    if type(item) == int:
        int_list.append(item)


# 2. feladat: Határozzuk meg egy lista legnagyobb és legkisebb elemének különbségét
lista = [random.randint(1, 1000) for i in range(10)]
retval = 0

lista = sorted(lista) #Ez mondjuk egy kicsit csalás
retval = lista[len(lista)-1] - lista[0]
print(lista)
print(retval)


# 3. feladat Határozzuk meg a lista legnagyobb és 2. legnagyobb elemét
max = lista[len(lista)-1]
second_max = lista[len(lista)-2]

print(f"A legnagyobb érték a listában: {max}\nA második legnagyobb érték a listában: {second_max}")

#rendesebb megoldás

lista = [random.randint(1, 1000) for i in range(10)]
retval = 0
min = lista[0]
max = lista[0]
for item in lista:
    if item > max:
        max = item
    if item < min:
        min = item

print("legnagyobb - legkisebb:", max-min)

# Egyszerű cserés rendezés (BUBBLE SORT :D)
for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Határozzuk meg egy tetszőleges függvény Zérus Helyét
#Könnyebb: csak egész szám lehet a ZH
#Nehezebb: mivan ha nem csak egész szám lehet a ZH
#mivan ha több zérushely van

def linear(x):
    return 2 * x -3

def absolute(x):
    return math.fabs(x - 2) - 10

def squared(x):
    return (x - 6) * (x + 2)

print(linear(1.5))

for i in range(-100, 100):
    if linear(i/10) == 0.0:
        print(f" LINEAR: {i/10}, {0}")
        break

for i in range(-100, 100):
    if absolute(i/10) == 0.0:
        print(f" ABSOLUTE: {i/10}, {0}")
        break

for i in range(-100, 100):
    if squared(i/10) == 0.0:
        print(f" SQUARED: {i/10}, {0}")
        

