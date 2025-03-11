
#1. feladat: Generáljunk egy listát, amiben vannak 0-tól 20-ig a számok

lista = []
for i in range(21):
    lista.append(i)
print(lista)

#2. feladat: Számok 5-15 -ig

lista = []
for i in range(5, 16):
    lista.append(i)
print(lista)

#3. feladat: [15, 30, 45, .... 150]

lista = []
for i in range(15, 151, 15):
    lista.append(i)
print(lista)

#4. feladat: [80, 79, 78, ... 54]

lista = []
for i in range(80, 53, -1):
    lista.append(i)
print(lista)

#5. feladat: [1, 4, 9, 16, 400] [négyzetszámok]

lista = []
for i in range(21):
    lista.append(i*i)
print(lista)

#6. feladat: [1, 1, 2, 3, 5, 8, 13] (fibonnaci) összesen mondjuk 30 elem

lista = [1, 1]
for i in range(2, 30):
    lista.append(lista[i-1]+ lista[i-2])
print(lista)

#7. feladat: [1, -2, 3, -4, ... -10]
lista = []
for i in range(1, 11):
    if i % 2 == 1:
        lista.append(i)
    else:
        lista.append(-i)
print(lista)

#8. feladat: [1, -1, 2, -2, 3, -3, .... 16, -16]

lista = []
for i in range(1, 17):
    lista.append(i)
    lista.append(-i)
print(lista)

#9. feladat [az első 20 prímszámot tartalmazza]

lista = [2]
k = 3
prime = True
while len(lista) < 20:
    prime = True
    for szam in lista:
        if k % szam == 0:
            prime = False
    if prime:
        lista.append(k)
    k += 1
print(lista)

#10. feladat: [100-999, azok a számok, amelyekben szerepel a 130] (132, 813)
lista = []
for i in range(100, 1000):
    szam = str(i)
    var = szam.find("13")
    if var != -1:
        lista.append(i)
print(lista)