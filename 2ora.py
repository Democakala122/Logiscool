szoveg = "A fekete cica nagyon szép volt"
print(szoveg)
print("A szöveg hossza: ", len(szoveg))

szoveg_szav = szoveg.split(" ")
print(szoveg_szav)

szoveg_az = szoveg.split("az") #ezt már tudtam
print(szoveg_az)

első_n = szoveg.find("n")
print("Az n itt fordul elő először: ", első_n)

első_az = szoveg.find("az") #elsőt megkeresi
print("Az az itt fordul elő először: ", első_az)

print(szoveg.startswith("A")) #true/false
print(szoveg.startswith("x"))
print(szoveg.startswith("."))
print(szoveg.startswith("k"))

szó = "kUtYa"
print(szó)
print(szó.capitalize()) #Kutya
print(szó.lower()) #kutya
print(szó.upper()) #KUTYA

print("a cica története".title()) #minden szót nagybetűvel kezd

print(szoveg.lower().count("a"))