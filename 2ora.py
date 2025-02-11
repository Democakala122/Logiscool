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

print(szoveg.lower().count("a")) #számol

thing1 = input("Type an object:\n")                 #tárgy1
thing2 = input("Type an object:\n")                 #tárgy2
adjektive = input("Give me an adjektive:\n")        #tulajdonság
song_name = input("Give me the name of a song:\n")  #zene
celebrity = input("Give me a celebrity name:\n")    #híresség
feeling = input("Give me a feeling\n")              #érzés
verb = input("Give me a verb:\n")                   #ige
place = input("Give me a place:\n")                 #hely
food = input("Give me a food:\n")                   #kaja
person = input("Give me a name:\n")                 #ember

print(f"""I just got back from a pizza party with {person}.
Can you believe we got to eat {adjektive} pizza in {place}?!
Everyone got to chose their own toppings.
I made {food} and {thing1} pizza, which is my favorite!
They even stuffed the crust with {thing2}. How {feeling}!
If that wasn't good enough already, {celebrity} was there singing {song_name}
I was so inspired by the music, I had to get up out of my seat and {verb}.""")