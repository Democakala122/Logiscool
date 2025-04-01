import re

# 1a feladat: Váltsunk át x kilogrammot grammba
def kgTog(kg):
    print(f'{kg}kg = {kg*1000}g')

# 1b feladat: Váltsunk át x grammot kilogrammba
def gTokg(g):
    print(f'{g}g = {g/1000}kg')

# Fahrenheit = (1.8 * Celsius) + 32
# Celsius = (Fahrenheit - 32) / 1.8
# 2a feladat: Fahrenheitből Celsiusba
def fToc(f):
    print(f'{f} Fahrenheit = {round((f - 32) / 1.8, 3)} Celsius')

# 2b feladat: Celsiusből Fahrenheitba
def cTof(c):
    print(f'{c} Celsius = {round((c * 1.8) + 32, 3)} Fahrenheit')

# 1 km = 0.62137 mérföld
# 3a feladat: Kilométerből mérföldbe
def kmTom(km):
    print(f'{km} km = {round(km * 0.62137, 3)} mérföld')
# 3b feladat: mérföldből Kilométerbe
def mTokm(m):
    print(f'{m} mérföld = {round(m / 0.62137, 3)} km')

# 4. feladat: Nézzük a számokat 1-től 75-ig
# Ha egy szám osztható 3-mal, akkor írjuk ki, hogy 'bim'
# Ha egy számban szerepel a 3-mas számjegy írjuk ki hogy 'bam'
# Ha oszható 3-mal és szerepel benne 3-mas akkor: 'bimbam'
for i in range(1, 76):
    if '3' in str(i):
        if i % 3 == 0:
            print(f'{i} : bimbam')
        else:
            print(f'{i} : bam')
    elif i % 3 == 0:
        print(f'{i} : bim')


# 5. feladat: Ellenőrizzük, hogy egy jelsző elég erős-e
# hossza 6 és 16 karakter közzött van
# van benne kis és nagybetű
# van benne szám
# van benne különleges karakter
password = ''
passed = False
numbers = [0,1,2,3,4,5,6,7,8,9]
specials = '<>#&@{}łí][Đđä\|Ä€Í$ß¤×÷"+!%/=()-_.:,?]'
while not passed:
    password = input('Please enter a password\n')
    if len(password) >= 6 and len(password) <= 16:
        if password.upper() != password and password.lower() != password:
            for number in numbers:
                if str(number) in password:
                    passed = True
            if passed:
                passed = False
                for i in range(len(specials)):
                    if specials[i] in password:
                        passed = True
                if passed:
                    break
                else:
                    print("Sorry password must contain special characters")
            else:
                print("Sorry password must contain numbers")
        else:
            print("Sorry password must contain small and capital letters")
    else:
        print("Sorry password must contain between 6 and 16 characters")


# 6. feladat: Adottak egy háromszög 3 oldalánakl hossza
# Adjuk, meg hogy a háromszög, derékszögű, egyenlő szárú szabályos, vagy egyik sem
def check_triangle(a,b,c):
    if a == b or a == c or b == c:
        print("Egyenlő szárú!")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Derékszögű!")


# 7. feladat: Egy futóversenyen ezek az időeredmények születtek:
nevek = ["Józsi", "Gábor", "Ferenc", "István", "János", "Károly"]
eredmények = [43.2, 49.6, 52.2, 43.8, 41.9, 46.0]
# Írjuk ki, hogy ki nyerte a versenyt

bestI = 0
for i in range(len(eredmények)):
    if eredmények[i] > eredmények[bestI]:
        bestI = i
print(nevek[bestI])

#Minden érték kiv(kg, g) 4 számjegyre kerekítve 
kgTog(10)
gTokg(1000)
fToc(72)
cTof(0)
kmTom(10)
mTokm(2)
check_triangle(3,4,5)