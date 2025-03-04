import random

i = 0
while i < 10:
    print(i, end=" ")
    i += 2
print()


#Számoljuk meg egy szám számjegyeit


num = 3424987342324
számjegy_számláló = 0
while num != 0:
    num //= 10
    számjegy_számláló += 1
print("Számjegyek száma: ", számjegy_számláló)


# Írjuk ki az n. fibinacci számot!
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89


n = 10
print(f"Fibanacci sorozat első {n} eleme: ")
a = 1
b = 1
while n > 0:
    print(a, end=" ")
    c = a+b
    a = b
    b = c
    n -= 1


#Melyik számra gondoltam?


num = random.randint(1, 100)
guessCount = 0
guess = 0
while guessCount < 7 and guess != num:
    guess = int(input("Tippelj egy egész számot!\n"))
    guessCount += 1
    if num > guess:
        print(f"Ennél nagyobb számra gondoltam. {7-guessCount} tipped maradt.")
    elif num < guess:
        print(f"Ennél kisebb számra gondoltam. {7-guessCount} tipped maradt.")

if guess == num:
    print(f"Gratulálok! Sikeresen kitaláltad, hogy a szám amire gondoltam a(z) {num} volt")
else:
    print(f"Hát nem találtad ki, hogy a szám amire gondoltam a(z) {num} volt")


# Írjunk egy programot ami, ezt írja ki:


"""
*
**
***
****
*****
******
*******
********
*******
******
*****
****
***
**
*
"""


# Olvassunk be folyamatosan számokat, amiket összegezünk, egész adig amíg 0-t nem írunk be


#5, 3, 4, 6, 0 -> 18
szam = int(input("Írj be egy számot:\n"))
ossz = 0
while szam != 0:
    ossz += szam
    szam = int(input("Írj be egy számot:\n"))
print(ossz)


