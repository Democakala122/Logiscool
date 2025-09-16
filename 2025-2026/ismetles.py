import random
print("Szia")

nev = input("Hogy hívnak?\n")

print(f"Szia {nev}!")

a = 321
b = 214
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

lista = [random.randint(-10,10) for i in range(20)]
print(lista)

# Hány negatív szám van a listában?
n = 0
for szam in lista:
    if szam < 0:    
        n += 1
print(f"A listában {n} negatív szám van")

# Írjuk ki a számok átlagát!
atlag = 0
for szam in lista:
    atlag += szam
atlag /= len(lista)
print(f"A listában a számok átlaga {atlag}")

# Mennyi a páros számok összege?

posszeg = 0
for szam in lista:
    if posszeg % 2 == 0:
        posszeg += szam
print(f"A listában a páros számok összege {posszeg}")

# Írjuk át a negatív számokat a listában a -10-szeresükre (-5 -> 50, -1 -> 10 stb...)

for i in range(0, len(lista)):
    if lista[i] < 0:
        lista[i] *= -10
    
print(f"Az átírt lista: {lista}")

# Írjunk egy fügvényt ami összeolvast két számot és visszaadja az eredményt
# (123, 456) -> 123456

def merge_nums(num1, num2):
    return int(str(num1) + str(num2))

print(merge_nums(12,421))

# Írjunk egy függvényt ami kap egy egész számot (n), illetve egy valamilyen másik értéket
# és visszaad egy n elemből álló listát aminek minden értéke (value)
# generate(3, "cica") -> ["cica", "cica", "cica"]

def generate(n, value):
    retlist = []
    for i in range(n):
        retlist.append(value)
    return retlist

print(generate(3, "sigam boi"))

# Írjunk egy függvényt ami kap egy listát, és visszaadja a listában lévő legnagyobb értéket!
def maxlist(lista):
    big = lista[0]
    for szam in lista:
        if szam > big:
            big = szam
    return big

print(maxlist([3,5,7,-1,4]))

# Írjunk egy függvényt ami kap egy nevet és kiírja, hogy "Hello {nev}" (nem ad vissza semmit)

def sayhi(nev):
    print(f"Hello {nev}!")

sayhi("Péter")
sayhi("Sanyi")

# Írjunk egy függvényt ami megkap egy egész számot és egy logikai értéket,
# ha logika igaz, akkor visszaadja a szám tizedesét
# ha hamis, akkor visszaadja a szám felét

def weirdnum(num, log):
    if log:
        return num/10
    else:
        return num/2
    
print(weirdnum(4, True))
print(weirdnum(4, False))
print(weirdnum(-42, True))
print(weirdnum(4.763, False))