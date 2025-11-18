
def factorial(n: int) -> int :
    """
    Kiszámolja a faktoriálisnak az értékét!
    tudod.
    """
    if type(n) != int:
        raise TypeError("A faktoriál függvénynek csak nem negatív egész számot lehet megadni!")
    if n < 0:
        raise ValueError("Negatív faktoriálist nem lehet megadni")
    if n < 2:
        return 1
    return n * factorial(n-1)

#Meg kell csinálni egy egy sajét cache cuccost (megjegyzi func értékét)
def fib():
    pass

def minimum(iterable):
    if len(iterable) == 0:
        raise ValueError("iterable cannot be empty")
    try:
        min_index = 0
        for i in range(len(iterable)):
            if iterable[i] < iterable[min_index]:
                min_index = i
        # Egyszerre visszaadjuk a legkisebb indexet és értéket is
        return (min_index, iterable[min_index])
    except:
        
