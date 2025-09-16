my_name = "Domó"
print("Az én nevem" + my_name)
print(f"Az én nevem {my_name}")

my_age = 21
print("Az én élétkorom: " + str(my_age))

pet_name = "Morzsi"
pet_age = 5
pet_species = "kutya"
print(f"A háziállatom neve: {pet_name}, {pet_age} éves és egy {pet_species}")

pet_name = "Cirmi"
pet_age = 2
pet_species = "cica"
print(f"A háziállatom neve: {pet_name}, {pet_age} éves és egy {pet_species}")

#TO DO 
name = input("Add meg a neved! ")
age = input("Add meg az életkorod! ")
print("A te neved: %s" %name)
print("A te neved %s és %d éves vagy" %(name, age))


num = 5
word = "auto"
is_boy = True
is_animal = False

if num:
    print("Ez egy szám")
if word:
    print("Ez egy karakter")
if is_boy:
    print("Ő egy fiú")
if is_animal:
    print("Ő egy állat")
else:
    print("Ő nem egy állat")

num1 = 12
num2 = 33
num3 = 66

if num1 > num2:
    print("Az első szám nagyobb mint a második")
if num1 < num2 and num2< num3: # and, or, <, >
    print("Kutya")
else:
    print(" A második szám nagyonbb mint az első")

a1= int(input("Kérem az első számot: "))
a2 = int(input("Kérem az első számot: "))

if a1>9:
    print("Ez a szám kétjegyű")
elif a1>a2:
    print("Az első szám nagyobb mint a második")

#SAJÁT FELADAT

number = int(input("Mi a pontszámod? "))
if number > 90:
    print("5-öst kaptál!")
elif number > 75:
    print("4-öst kaptál!")
elif number > 60:
    print("3-öst kaptál!")
elif number > 40:
    print("2-öst kaptál!")
else:
    print("1-öst kaptál!")
