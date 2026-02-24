import os

PATH_FORRAS = os.path.join(os.path.dirname(__file__), 'forras')
"""
a = input('Add meg az osztandót! ')
b = input('Add meg az osztót! ') 

# print(f"{a} / {b} = {a/b}") -- TypeError: unsupported operand type(s) for /: 'str' and 'str'

# Ha nem számot adunk meg -- ValueError: could not convert string to float: '2ű'

# Ha b = 0 -- ZeroDivisionError: float division by zero
try: 
    print(f"{a} / {b} = {float(a)/float(b)}")
except TypeError:
    print('Típus hiba!')
except ValueError:
    print('Mindenképpen számot adj meg!')
except ZeroDivisionError:
    print('0-val osztani nem szabad osztani!')
except Exception:
    print('ismeretlen hiba!')
finally:
    print('Osztás program vége! ')
"""

path = os.path.join(PATH_FORRAS, 'test')
try:
    with open(path) as f:
        print(f.read(50))
except FileNotFoundError:
    print('nincs ilyen fájl: ', path)
except PermissionError:
    print('nincs permissioned kinyitni a fájlt-')
except Exception as ex:
    print("HIBA")
    print(ex.args[1])

def fakt(n):
    if type(n) != int:
        raise TypeError("The factorial funtion only takes positive integers!")
    if n < 0:
        raise ValueError("The number must be positive!")
    if n == 0:
        return 1
    else:
        return n * fakt(n-1)
    
# print(fakt(4.1)) -- RecursionError: maximum recursion depth exceeded

num = 4.1
try:
    print(fakt(num))
except TypeError as ex:
    print('Típus hiba!')
    print(ex)
except ValueError as ex:
    print('Érték hiba!')
    print(ex)
except Exception as ex:
    print('ismeretlen hiba!')
    print(ex)

# Feladat: Írj egy függvényt ami megkap egy évszámot és kiszámolja hogy hány év telt el azóta.
# Ha nem integert adunk, meg akkor dobjunk típus hibát.
# Ha a megadott évszám nagyobb mint 2026 (vagy aktuális évszám, bónusz feladat), akkor dobjunk VAlue errort
def evszamolo(ev):
    if type(ev) != int:
        raise TypeError("Az év int!")
    if ev > 2026:
        raise ValueError("Az év nem lehet 2026 nagyobb!!")
    return 2026 - ev


# A függvény használatára írjunk egy programot, ami bekér a felhasználótól egy évszámot.
# És kiírja a függvény eredményét. MINDEN LEHETSÉGES HIBÁT kezelj le!
try: 
    print(f'{evszamolo(input('Add meg az évet!'))} éves vagy!')
except TypeError as ex:
    print("Az év integer!")
    print(ex)
except ValueError as ex:
    print(("Az évszám nem lehet 2026 nagyobb!!"))
    print(ex)
except Exception as ex:
    print('Ismeretlen hiba!')
    print(ex)
finally:
    print('evszamolo program lefuttatása sikeres!')

def avarage(lista):
    if type(lista) != (list or tuple):
        raise TypeError("Listát kell megadni")
    if len(lista) == 0:
        raise ValueError("A lista hossza nem lehet 0!")
    for szam in lista:
        if type(szam) != (int or float):
            raise TypeError("A listában csak számok lehetnek!")
    return sum(lista) / len(lista)


