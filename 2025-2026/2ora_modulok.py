from random import randint, randrange, seed
from functools import cache
import math
import numpy as np
import matplotlib.pyplot as plt #pip install matplotlib.pyplot
from matplotlib.colors import LinearSegmentedColormap

def intro():
    #Mivel a gépek nem teljesen randomok, 
    # ha ugyanazt a seed-et adod meg ugyanazokat a random számokat fogod kapni

    seed(123)
    print(randint(5,25))
    print(randint(5,25))

    print(math.pi)
    print(math.tau)
    print(math.e)
    print(math.sqrt(2))
    print(math.inf) # mindennél nagyobb
    print(math.nan)

    # + minden jó matematikai függvény

    print(math.sin(60))
    print(math.ceil(4.00002))
    print(math.floor(4.00002))

    radius = 5
    print(f"A {radius} egység sugarú kör területe: {round(radius**2 * math.pi, 4)}")
    print(f"A {radius} egység sugarú kör területe: {round(radius**2 * 3.14, 4)}")

def array():
    tomb = np.array([1,2,3,4,5])
    print(tomb)
    print(type(tomb))
    linear = np.linspace(-5, 4.9, 100) #eloszta egyenletesen megadott számokat
    print(linear)
    print(linear.shape) # dimenziók 1*100
    linear = linear.reshape(5,5,4) # dimenziók megadása <- TÖk JÓ CUCC
    print(linear)
    print(linear.shape) # dimenziók 
    linear = linear.reshape(20, -1) #kitalálja hány oszlop kell legyen
    print(linear)
    print(linear.shape)

mtx = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,1,0],
    [0,1,1,0,0,1,1,0],
    [0,0,0,1,1,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,0,0,1,0,0]
]
my_cmap = LinearSegmentedColormap.from_list("creeper", ["green", "black"])
plt.imshow(mtx, cmap=my_cmap)
plt.axis("off")
plt.show()

