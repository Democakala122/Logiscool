# 1. feladat: olvassuk be valaki születési dátumát (yyyy-mm-dd) és ez alapján
# Határozzuk meg, hogy hány napos az illető
today = [2025, 4, 15]
birth_date = input("add meg a születési dátumod (yyyy-mm-dd)\n")
birth_date = birth_date.split("-")
for i in range(len(birth_date)):
    birth_date[i] = int(birth_date[i])

days = 0
"""while str(birth_date) != str(today):
    if birth_date[2] != 30:
        birth_date[2] += 1
    else:
        if birth_date[2] != 12:
            birth_date[0] += 1
            birth_date[1] = 1
            birth_date[2] = 1
        else:
            birth_date[1] += 1
            birth_date[2] = 1
    days += 1
    print(birth_date)
"""


# 2. feladat: Döntsük el két stringről hogy anagrammák-e
# Pontosan ugyanazok a karakterek vannak benne
word1 = input("word1:\n")
word2 = input("word2:\n")
"""
def counter(word):
    Returnval = {}
    for betu in word:
        Returnval[betu] += 1
    return Returnval

if counter(word1) == counter(word2):
    print('yep')
else:
    print('nah')
"""
# 3. feladat: Hány autónak kell lassítania? 
# egy autó nem mehet gyorsabban mint az előtte lévő
cars = [43, 76, 32, 54, 77, 91, 23, 45, 78, 99, 62, 48, 90, 99, 102]
for i in range(len(cars)-1):
    for j in range(len(cars)-1):
        if cars[j] > cars[j+1]:
            cars[j] = cars[j+1]
print(cars)            
