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


# Írjunk egy programot, ami eldönti egy számról, hogy prímszán-e! While ciklussal
szam = int(input("Írj be egy számot amiről szeretnéd tudni, hogy prímszám-e: \n"))
num = 2
while num < szam-1 and szam % num != 0:
    num += 1

if szam % num == 0:
    print("Ez nem egy prímszám")
else:
    print("Ez egy prímszám")