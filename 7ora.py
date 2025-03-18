#operátorok = műveleti jelek
# +, -, *, //, %, >, =, ==, >= stb

#aritmetikai (matematikai)
print(3 + 5) # int
print(2 - 1) # int
print(4 * 3) # int
print(40 / 8) # float 
#nem tudjuk garantálni, hogy egész szám legyen, ezért az eredményt float-ként tároljuk el

print(42 / 8) # float <- itt kell mert ez 5.25
print(42 // 8) # ez int, mert ez maradék nélküli osztás
print(40 // 8) # itt is

#Maradékos osztás: (%) megadja az osztási maradékot
print(10 % 7) # 3

#Hatványozás (**)
print(2 ** 32) #4294967296
print(10 ** 3) #1000

#Gyökvonás hatványozással
#négyzetgyök 16**(1/2)
#6. gyök 16**(1/6)
print(2**(1/2)) # float

# + összeadás
# - kivonás
# * szorzás
# / osztás
# // maradék nélküli osztás
# % osztás maradéka
# ** hatványozás, gyökvonás törtekkel



# Értékadó operátorok (szinte bármi amiben =-jel van)
#egy változónak értéket ad
num = 10 
print(f"num = {num}") # 10
num += 5 # A num értékéhez hozzá ad 5-öt
print(f"num = {num}") # 15
num -= 3
print(f"num = {num}") #12
num *= 4
print(f"num = {num}") #48
num /= 2
print(f"num = {num}") #24.0 num FLOAT lesz
num //= 2
print(f"num = {num}") #12 ha num FLOAT akkor az marad, amúgy int
num **= 2
print(f"num = {num}") #144 ha num FLOAT akkor az marad, amúgy int



#Összehasonlító operátorok (True vagy False értéket adnak)
#Két értéket összehasonlít
print(5 > 3) # True
print(5 < 2) # False
print(5 == 8) # False
print(5 >= 5) # True
print(4 <= 2) # False
print(4 != 2) #True


#Logikai operátorok
#Logikai értékekkel kezdenek valamit
# (ÉS VAGY, NEM)
#Logikai érték eredményük (True, False)
print(5 > 3 and 3 > 4) # True and False -> False
print(5 > 1 or 3 > 4)# True and False -> True
print(not 5 > 1)

#Logikai kapuk:
# A | B | A and B | A vagy B | nem A | nem B 
# i | i |    i    |     i    |   h   |   h
# i | h |    h    |     i    |   h   |   i
# h | i |    h    |     i    |   i   |   h
# h | h |    h    |     h    |   i   |   i
