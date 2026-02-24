szam1 = int(input("Adj meg egy számot! "))
szam2 = int(input("Adj meg még egy számot! "))

print(szam1 + szam2)
print(szam1 - szam2)
print(szam1 * szam2)
print(szam1 // szam2)
print(szam1 % szam2)
print(szam1 ** 2) 
# SZÉPEBBRE, (szebbre)

osszeg = int(input("Add meg az összeget! "))
penzek = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
kell = []

for i in range(len(penzek)):
    kell.append(0)

i = 0

while osszeg > 0:
    if osszeg >= penzek[i]:
        osszeg -= penzek[i]
        kell[i] += 1
    else:
        i += 1

for i in range(len(penzek)):
    print(f"{penzek[i]} Ft: {kell[i]} db")