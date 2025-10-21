import random

def func(x):
    for i in range(10):
        if i == x:
            return
    print('függvény vége')

func(4) # Nem történik semmi
func(46) # Kiírja, hogy vége a függvénynek

# Felsoroló függvények: (yield)

def negyzet_szamok():
    i = 1
    while True:
        yield i **2 # Visszaadja az i négyzetét, de nem állítja le a függvényt
        i += 1

for num in negyzet_szamok():
    print(num, end=" ")
    if num > 100:
        break

def myrange(upperBound):
    i = 0
    while i < upperBound:
        yield i
        i += 1

for i in myrange(5):
    print(i, end=" ") # 0 1 2 3 4 
print()

# Feladat: Készítsünk egy felsoroló függvényt, ami két index közötti fibonacci számot határozza meg
def fib_gen(from_n, to_n):
    if from_n < 1:
        return "minimum 1 legyen a from num"
    for num in range(from_n, to_n):
        yield ""

def yield_evens(lista):
    for item in lista:
        if item % 2 == 0:
            yield item

for item in yield_evens([5,4,67,7,3,5,7,4,5,123,763]):
    print(item, end=" ")
print()

# Írjunk egy generátor függvényt ami az
# a(n) = a(n-1) + 5
# a(1) = 2
# sorozat elemeit sorolja
def a(n):
    if n == 1:
        return 2
    else:
        return a(n-1) + 5
    
def a_gen(n):
    for i in range(1, n+1):
        yield a(i)

print('hey')

for item in a_gen(5):
    print(item, end=" ")


# Írjunk egy generátor függvényt, ami megkap egy stringet és felsorolja a stringben
# található összes magánhangzót
maghang = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
def string_counter(string):
    for betu in string:
        if betu in maghang:
            yield betu

for item in string_counter('szeretem az almákat, de úgy nagyon tényleg'):
    print(item, end=" ")


# Írjunk egy prímszám generáló függvényt, a függvény egy paramétert kap (n), az első n
# prímszámot kell legenerálnunk
def elso_prim(n):
    primek = [2]
    i = 2
    isPrime = True
    while len(primek) < n:
        isPrime = True
        i += 1
        for prim in primek:
            if i % prim == 0:
                isPrime = False
        if isPrime:
            primek.append(i)
            yield i



for item in elso_prim(10):
    print(item, end=" ")
            
# Készítsünk egy olyan függvényt, ami egy bármilyen szűrűt alakalmaz egy listát

def is_even(num):
    return num % 2 == 0

def is_two_digit(num):
    return 10 <= num and num <= 99


def filter_list(lista, func):
    for item in lista:
        if func(item):
            yield item

lista = [random.randint(1,100) for i in range(20)]
evens = [i for i in filter_list(lista, is_even)]
two_digits = [i for i in filter_list(lista, is_two_digit)]

print()
print(lista)
print(evens)
print(two_digits)