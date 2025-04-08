import random

#1 feladat: szedjük ki a duplikációkat a listából
szamok = [4, 1, 3, 9, 2, 8, 1, 8, 2, 4, 6, 3, 1, 0, 2, 5, 3, 2]

seen = []
i = 0
for i in range(len(szamok)):
    if szamok[i] not in seen:
        seen.append(szamok[i])
print(seen)