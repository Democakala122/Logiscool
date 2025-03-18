#1. feladat: Adott 2 lista
#egyesítsük őket egy új listában, hogy ne legyenek duplikációk
lista1 = [43, 12, 75, 23, 99]
lista2 = [13, 54, 43, 12, 92, 12, 11]

lista3 = []
lista3 = lista1[:]
for szam in lista2:
    if szam in lista3 != True:
        lista3.append(szam)
print(lista3)


#2. feladat: Jelenítsünk meg egy a, b oldalú téglalapot
#Kimenet:
#######
#######
#######
#######
#######
a = 5
b = 10
import math

for i in range (a):
    print("a" * int(math.fabs(b)))


#3. feladat: Szöveg kódolás
# kimenet = Kdlifgmetasöeeóon oo z   zvgt
bemenet =  "Kódolni fogom ezt a szöveget"
index = 1
kimenet = ""
for betu in bemenet:
    if index % 2 == 1:
        kimenet += betu
    index += 1
index = 1
for betu in bemenet:
    if index % 2 == 0:
        kimenet += betu
    index += 1
print(kimenet)



#4. feladat: Olvassunk be egy számot és írjuk ki a szorzó tábláját
#Kimenet:
# 1 * 3 = 3
# 2 * 3 = 6
# 3 * 3 = 9
#....
# 10 * 3 = 30
num = int(input("Add meg a számot!\n"))
for i in range(1, 11):
    print(f"{i} * {num} = {i*num}")