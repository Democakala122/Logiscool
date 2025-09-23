# A rekurzív függvény egy olyan függvény ami, önmagát hívja meg

# pl. Faktoriális:
# 4! = 4 * 3 * 2 * 1 = 24
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1

# n! = n * (n-1)!
# fakt(n) = n * fakt(n-1)   

def fakt(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * fakt(n-1)

print(fakt(10))

# Írjunk egy függvényt az "a" rekurzív sorozat n. elemének kiszámítására
# a(n) = 5 + a(n-1)
# a(1) = -5
# a(3) = 5 + a(2) = 5 + 5 + (1) = 5 + 5 + (-5) = 5

def a(n: int) -> int:
    if n <= 1:
        return -5 
    return 5 + a(n-1)

print(a(8))

# fibinaccio
# fib(n) = fib(n-1) + fib(n-2)

def b(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return b(n-1) + b(n-2)

print(b(20))

# c(n) = 3 * c(n-1) + 7     c(1) = -2
def c(n: int) -> int:
    if n == 1:
        return -2
    return 3 * c(n-1) + 7

# d(n) = d(n-1)**2 - 9 * d(n-2) - 10    d(1) = 0    d(2) = 3
def d(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 3
    return d(n-1)**2 - 9 * d(n-2) - 10

# e(n) = 2**(e(n-1))    e(1) = 0
def e(n: int) -> int:
    if n == 1:
        return 0
    return 2**(e(n-1))

print(c(2))
print(d(5))
print(e(3))

print(4 - 2 * 2)

from functools import cache
#le menti eredményeket 
# g(n) = n + g(n-1), g(n-1) = n-1 + g(n-2) ....
# cache, ha már egy func levolt futottva megjegyzi a return értékét.

@cache
def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

i = 2
while True:
    if i > 200:
        break
    print(f"fib({i}) = {len(str(fib(i)))}")
    i += 1

# Írjunk egy rekurzív függvényt, ami meghatározza egy lista elemeinek az összegét
# sum([]) = 0
# sum([n]) = n
# sum([n, m ]) = n + sum([m])

def sum(lista: list) -> int:
    if len(lista) == 1:
        return lista[0]
    return lista[0] + sum(lista[1:])

print(sum([1,2,3,4,5]))
    






