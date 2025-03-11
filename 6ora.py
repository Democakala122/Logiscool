nevek = ['Andárs', 'Béla', 'Cecil', 'Dénes', 'Elemér', 'Ferenc']
print(nevek)
print(type(nevek))
print('A lista elemszáma: ', len(nevek))

print(nevek[0]) # András
print(nevek[3]) # Dénes
print(nevek[len(nevek)-1]) #utolsó elem
#Pythonban, megadhatunk negatív indexet
print(nevek[-1]) # hátulról 1. Ferenc
print(nevek[-4]) # hátulról 4. Ferenc

#Intervallumos indexelésre is van lehetőségünk
print(nevek[2:5]) #2. indextől 5.-ig, 5. már nem lesz benne
print(nevek[:4])  #Ha nem írunk semmit akkor a lista elejétől kezdem itt sincs benne 4. index
print(nevek[2:])  #2. indextől a végtől a végéig itt benne van az utolsó elem is

print(nevek[:]) # Az összes eleme
nevek2 = nevek
print(nevek2)
#Amikor egy listát egyenlővé teszünk egy másikkal, akkor valójában nem készül új másolat
#Csak új elnevezést hozzunk létre annak a listának
#Ezért hasznos [:] ez

nevek2 = nevek[:]
nevek2[2] = "Cica"
print(nevek2)
print(nevek)

#2. lehetőség

nevek2 = nevek.copy()
nevek2[2] = "Cirmos"
print(nevek2)
print(nevek)

#lista eleminek a megfordítása:

nevek = nevek[::-1]
print(nevek)

#Milyen lehetőségeink vannak egy lista bejárására?

#Klasszik: while (elől tesztelős) ciklus

i = 0
while i < len(nevek):
    print(nevek[i], end=" ")
    i += 1
print()

# For ciklus

for i in range(len(nevek)):
    print(nevek[i], end=" ")
print()

# foreach ciklus

for item in nevek:
    print(item, end=" ")
print()

#Vegyítvea két ciklust

for index, item in enumerate(nevek):
    print(f"{index}: {item}", end=" ")
print()