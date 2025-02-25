# írjuk ki az első 10 természetes számot

i = 1
while i <= 10:
    print(i)
    i += 1
print()

lista = []
bemenet = "default"
while bemenet != "":
    bemenet = input("Add meg a lista következő elemét!")
    if bemenet != "":
        lista.append(bemenet)
print(lista)

for i in range(10): # 0-9
    print(i, end=" ")
print()

for i in range(5, 15): #5-14
    print(i, end=" ")
print()

for i in range(2, 100, 10): #2-92
    print(i, end=" ")
print()

for i in range(2, 100, -10): #2-92
    print(i, end=" ")
print()

lista = ["Anna", "Béla", "Cecil", "Dani"]
for item in lista: # minden item
    print(item, end=" ")

for i in range(len(lista)):
    print(lista[i], end = " ")
print()

