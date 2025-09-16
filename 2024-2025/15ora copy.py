import random
import tkinter # Külső könyvtár (alapból nem része a pythonnak)
# Ezt külön telepíteni kell

def generate_puzzle():
    puzzle = ""
    while len(puzzle) != 4:
        digit = random.randint(0, 9)
        if str(digit) not in puzzle:
            puzzle += str(digit)
    return puzzle

puzzle = generate_puzzle()# pl. 6843

gameOn = True
tipp = ""
tippek = 0

def check_tipp():
    tipp = "1234"
    if len(tipp) != 4 or not tipp.isdigit() or len(set(tipp)) != 4:
        return
    jo_szamok = 0
    jo_szamok_jo_helyen = 0
    for i in range(len(tipp)):
        if tipp[i] == puzzle[i]:
            jo_szamok_jo_helyen += 1
        elif tipp[i] in puzzle:
            jo_szamok += 1
    tippek += 1
    if jo_szamok_jo_helyen == 4:
        gameOn = False
    else:
        print(f"jó számok, jó helyen száma: {jo_szamok_jo_helyen}")
        print(f"jó számok, de nem jó helyen száma: {jo_szamok}")

while gameOn:
    tipp = input("Adj meg száámjegyet szóközek nélkül (pl.: 0123)\n")
    