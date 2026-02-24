import os
import random

# dictionary (szótár) adatszerkezet


szotar = {} # Egy üres dictionaryt hoz létra
szotar = {
    "alma": "apple",
    "ananász": "pineapple",
    "bögre": "mug",
    "citrom": "lemon",
    "citrom": "citrus", # lemonról átíródik citrusra
    "kukorica": "corn"
}

print(szotar)
print(type(szotar)) # <class 'dict'>
print(len(szotar)) # 5
print(szotar["bögre"]) # mug
print(szotar["citrom"]) # mug

# Dictionary kulcs-érték párokat tárol
# Egy kulcs csak egyszer szerepelhet egy szótárban
# Az értékekre nincs ilyen megkötés


# Dictionary-k bejárása

def opcio1(dict):
    for item in dict.keys(): #.keys() nem kell
        #print(item)  ananász, alma, bögre, ... (A dictionary kulcsain megy végig)
        #print(type(item))  string
        print(f"{item} -> {szotar[item]}")

def opcio2(dict):
    # Fő gond, hogy értékből nem tudjuk megkapni a kulcsot
    for item in dict.values():
        print(item)

def opcio3(dict): # GOAT
    for item in dict.items(): # tuple-be vissza adja a kulcspárokat
        print(item, type(item))

    for key, value in dict.items():
        print(f"{key} -> {value}")

szotar["könyv"] = "book" # új elem hozzáadása

# Szerepel-e egy adott kulcs a dictionaryben?
if "billentyűzet" in szotar.keys():
    del szotar["billentyűzet"] # kitörli billentyűzetet
else:
    szotar["billentyűzet"] = "keyboard"

with open(os.path.join(os.path.dirname(__file__), 'forras', "something.txt"), encoding="utf-8") as f:
    szoveg = f.read()
    szoveg = szoveg.replace('.', "")
    szoveg = szoveg.replace(',', "")
    szoveg = szoveg.replace('"', "")
    szoveg = szoveg.replace(';', "")
    szoveg = szoveg.replace(':', "")
    szoveg = szoveg.replace('\n', " ")
    szoveg = szoveg.replace("“", "")
    szoveg = szoveg.replace("”", "")
    szoveg = szoveg.replace("?", "")
    szoveg = szoveg.replace("’s", "")
    szoveg = szoveg.lower()
    szoveg = szoveg.split(" ")

word_counter = {}

for word in szoveg:
    if word in word_counter.keys():
        word_counter[word] += 1
    else:
        word_counter[word] = 1

# A dictionary nem rendezhető, mert nem számít az elemek sorrendje 

# Ha mégis rendezni akarjuk, akkor alakítsuk listává, majd vissza dicitonaryvá

"""
word_counter = dict(sorted(list(word_counter.items()), key=lambda x: x[1], reverse=True)) # A sorted a tuple első eleme alapján sortírozza
print(word_counter)

# Átlagosan hányszor fordul elő egy szó?
összeg = 0
for key, value in word_counter.items():
    összeg += value
print(f"egy szó átlagosan {round(összeg/len(word_counter), 2)} alkalommal fordul elő. ")
"""

players = []
     
for i in range(10):
    player = {}
    player['class'] = random.choice(["Mage", "Warrior", "Priest", "Paladin", "Rogue"])
    player['level'] = random.randint(1, 80)
    player['stamina'] = random.randint(50, 280)
    player['strength'] = random.randint(50, 280)
    player['intellect'] = random.randint(50, 280)
    player['armor'] = random.randint(50, 280)
    player['speed'] = random.randint(50, 280)
    players.append(player)

#print(players)

# 1 feladat: Írjuk ki a legmagasabb szintű játékost.
max_sz = 0
max_nev = 0
for i in range(len(players)):
    if players[i]['level'] > max_sz:
        max_sz = players[i]['level']
        max_nev = i
print(f"A legjobb játkos a {max_nev}. játékos {max_sz}-szintel.")

# 2 feladat: Mennyi a játékosok átlagos intelligencia szintje?
osszeg = 0
for player in players:
    osszeg += player['intellect']
print(f"A játékosok átlag intellektje: {osszeg/len(players)}")

# 3 feladat: Hány Warrior van a csapatban?
warriornum = 0
for player in players:
    if player['class'] == "Warrior" :
        warriornum += 1
print(f"A csapatban {warriornum} Warrior van.")
# 4 feladat: Van-e legalább 60-as szintű Paladin a játékosok között?
isW = False
for player in players:
    if player['class'] == "Paladin" and player['level'] >= 60:
        isW = True
        break

if isW:
    print("A csapatban van level 60-as paladin.")
else:
    print("A csapatban nincs level 60-as paladin.")
# 5 feladat: Írjuk ki, hogy melyik class-ból hány darab van a csapatban.
classes = {}
for player in players:
    if player['class'] in classes.keys():
        classes[player['class']] += 1
    else:
        classes[player['class']] = 1

for role, value in classes.items():
    print(f"{role}: {value}")