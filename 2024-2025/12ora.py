#feladat: Számoljuk meg hogy egy stringben hány mássalhangzó szerepel
szöveg = "A kis cica nagyon aranyos"
magánhangzók = 'eioöüóőúaéáűíEIOÖÜÓŐÚŰÁÉAÍ'
mássalhangzók = 'qQwWrRtTzZpPsSdDfFgGhHjJkKlLyYxXcCvVbBnNmM'

magán = 0
mással = 0
szóköz = 0
special = 0

for betu in szöveg:
    if betu in magánhangzók:
        magán += 1
    elif betu in mássalhangzók:
        mással += 1
    elif betu == "":
        szóköz += 1
    else:
        special += 1
print(szöveg)
print(f'Ebben a szövegbem {magán} magánhangzó, {mással} mássalhangzó, {szóköz} szóköz és {special} speciális karakter van. A szöveg {len(szöveg)} hosszú')

#2. feladat: Határozzuk meg egy szám számjegyeinek összegét
eszam = 3423432
szamjegyosszeg = 0
for szam in str(eszam):
    szamjegyosszeg += int(szam)
print(szamjegyosszeg)

#3. feladat: Olvassuk be egy tört számlálóját és nevezőjét, majd hozzuk a lehető legyegyszerűbb alakra a törtet pl.: 100/12 -> 25/3
szamlalo = 100
nevezo = 14

maxkoz = 1
if szamlalo < 0:
    szamlalo *= -1
if nevezo < 0:
    nevezo *= -1
for i in range(2, min(szamlalo, nevezo)+1):
    if nevezo % i == 0 and szamlalo % i == 0:
        maxkoz = i

print(f"{szamlalo}/{nevezo}, legegyszerűbb alakja a {int(szamlalo/maxkoz)}/{int(nevezo/maxkoz)}")

#4. feladat: Legyen adott 2 tört, szorozzuk össze őket, és írjuk ki az eredményt a legegyszerűbb alakban
szamlalo1 = 1
nevezo1 = 2
szamlalo2 = 3
nevezo2 = 4

szamlalo = szamlalo1*szamlalo2
nevezo = nevezo1*nevezo2
maxkoz = 1
for i in range(2, min(szamlalo, nevezo)+1):
    if nevezo % i == 0 and szamlalo % i == 0:
        maxkoz = i

print(f"{szamlalo1}/{nevezo1} és a {szamlalo2}/{nevezo2} szorzata {szamlalo}/{nevezo}, a legegyszerűbb alakja a {int(szamlalo/maxkoz)}/{int(nevezo/maxkoz)}")

#5. feladat: Döntsük el egy számrül hogy tökéletes-e!
#Egy szám akkor tökéletes, ha az osztóinak összege (önmagát kivéve), pont az a szám:
#pl. 6 = 1 + 2 + 3 = 6
szam = 0
while szam < 1000:
    szam += 1
    osszeg = 0
    for i in range(1, szam):
        if szam % i == 0:
            osszeg += i
    if osszeg == szam:
        print(f"A {szam} egy tökéletes szám!")

#6. feladat: Adott egy lista
#Határozzuk meg a lista elemeinek átlagát
#Medián (középső elem) [3, 6, 9, 13, 15, 17, 18, 20] 13
#Ha 2 elem középső akkor annak a kettő elem átlaga
def median(lista): # kell ide SORTED
    if len(lista) % 2 == 1:
        return lista[len(lista)//2]
    else:
        return (lista[len(lista)//2-1]+lista[len(lista)//2])/2

print(median([1,2,3,4,5,6,7,8,9,10]))

#6b. feladat: Szórás - A listában egy elem átlagosan, mennyivel tér el az átlagtól (Mediántól)
def szoras(lista):
    media = median(lista)
    val = 0
    for szam in lista:
        if media > szam:
            val += media-szam
        else: #absolute értéket is lehetne itt használni
            val += szam-media
    return val / len(lista)
    

print(szoras([1,2,3,4,5,6,7,8,9,10]))

#AZ EGÉSZET MEGCSINÁLNI DEF-EL ÉS AZ UTOLSÓBA SORTED KELL
# math.randint(-20,200) for i in range(30)) random lista generálásához