# A tuple szinte ugyanaz, mint a lista, a fő különbség , hogy nem múdosítható

myTuple = (5, 2, 6)
print("myTuple:", myTuple)
print("type(myTuple)", type(myTuple))
print("mytuple[1] =", myTuple[1])
print("mytuple[0:2] =", myTuple[0:2])

# Nem módosítható 

# myTuple[1] = 8
# "asd"[2] = 2 # a string is ilyen
#myTuple.append(3) #AttributeError: 'tuple' object has no atribute 'append'
#myTuple += 1 # TypeError: can only concatenate tuple (not "int") to tuple

myTuple += (3,) 
print(myTuple) # (5, 2, 6, 3)

empty_tuple = ()
print(empty_tuple) # ()
print(type(empty_tuple)) 

one_element_tuple = (3) # így int lesz
# A (3) kifejezést aritmetikai kifejezésként értlemezi -> 3 értékű intre fog kiértékelődni 

one_element_tuple = (3, )
print(one_element_tuple) # (3,)
print(type(one_element_tuple)) # <class 'tuple'> 

# Az elemek típusait szabadon lehet keverni 
myTuple = (45, True, "kiscica", 3.13, 14, False, [1,2,3], (9,8))

print(myTuple)

#tuple comprehension
myTuple = tuple(i for i in range(1, 11))
print(myTuple)

# Operátorok tuple-re:

tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = (3,2,1)
tuple4 = (4,5,6)

# Egyenlőség vizsgálat
print(tuple1 == tuple2) # False
print(tuple1 == tuple3) # False
print(tuple2 == tuple4) # True

print(f"tuple1 * 3  = {tuple1 * 3}") # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(f"tuple1 + 3 = TypeERROR")
print(f"tuple1 + tuple2 = {tuple1 + tuple2}") # (1, 2, 3, 4, 5, 6)

#1 feladat


# 2. feladat 
összeg = 0
for item in myTuple:
    összeg += item
print("Összeg: ", összeg)

# 3. feladat: Töröljük a listából a nem tuple típusú objektumokat
lista = [4, (1,3,4), [1, 9, "asd"], "asd", (1,), (5,9,1,2), True]
new_lista = []
for item in lista:
    if type(item) == tuple:
        new_lista.append(item)
lista = new_lista[:]
print(lista)

# 4. feladat: Határozzk meg a tuple-ök elemeinek az átlagát
myTuple = ((1, 2, 3), (40, 13), (91, -23, 10), (-1, 0, 40, -50, 33))
lista = []
for ituple in myTuple:
    osszeg = 0
    for szam in ituple:
        osszeg += szam
    lista.append(osszeg/len(ituple))
print(lista)

# 5. feladat: Fordítsuk meg egy tuple elemeit
myTuple = (1, 2, 3, 4, 5, 6)   # -> (6, 5, 4, 3, 2, 1)

rev_myTuple = (item for item in myTuple[::-1])

lista = [i for i in range(len(myTuple))]
for i in range(len(myTuple)):
    lista[len(myTuple)-1-i] = myTuple[i]

def make_it_tuple():
    for szam in lista:
        yield szam

rev_myTuple = tuple(make_it_tuple())
print(rev_myTuple)

# 6. feladat: Ugyan ennek a tuplenek vágjuk le az első és utolsó elemét,
# majd mentsük el egy új tuple-be
new_tuple = myTuple[1:-1]
print(new_tuple)

# 7. feladat: Határozzuk meg, hogy egy tuple-ben melyik indexen található az első kétjegyű szám
def two_num_tuple(atuple):
    for i in range(len(atuple)):
        if type(atuple[i]) == int:
            if atuple[i] >= 10 and atuple[i] <= 99:
                return i
            
print(two_num_tuple((6,7,3,"sss", ["nem", 43], 24, 56)))

# 8. feladat:  Számoljuk ki a vector-műveletek eredményét
a = (3, 5)
b = (-1, 3)
c = (2, -1)
# Határozzuk meg az       a + 2b - 3c vektort
def add_vec(vec1, vec2):
    return (vec1[0]+vec2[0], vec1[1]+vec2[1])

def sub_vec(vec1, vec2):
    return (vec1[0]-vec2[0], vec1[1]-vec2[1])

def skal_vec(vec1, mult):
    return(vec1[0] * mult, vec1[1]* mult)

print(sub_vec(add_vec(a, skal_vec(b, 2)), skal_vec(c, 3)))