import os 

szerverek = []

path = os.path.join(os.path.dirname(__file__), "minecraft-adatok.txt")

with open(path, encoding="utf-8") as f:
    next(f)
    for line in f:
        line = line.strip().split(';')
        szerver = {'nev': line[0],
                   'mod': line[1],
                   'jatekosok': int(line[2]),
                   'havi_dij': int(line[3])}
        szerverek.append(szerver)


#1. Írd ki, hogy hány szerver van összesen!
print(f"Szerverek száma: {len(szerverek)}")

#2. Írd ki, hogy melyik szerveren van a legtöbb játékos és hány fő!
max_index = 0
for i in range(1, len(szerverek)):
    if szerverek[i]['jatekosok'] > szerverek[max_index]['jatekosok']:
        max_index = i

print(f'A legtöbb játékos a {szerverek[max_index]['nev']} szerveren van, {szerverek[max_index]['jatekosok']} fő.')

#3. Írj egy függvényt vip_ar néven, ami paraméterként megkapja a havi díjat és
#visszaadja, hogy mennyibe kerülne a VIP csomag, ami 50%-kal drágább!
def vip_ar(ar):
    return int(ar * 1.5)

#4. Kérj be a felhasználótól egy szerver nevet, majd írd ki, hogy az adott szerveren
#mennyi lenne a VIP csomag ára! (az előző feladatban lévő függvényt használd fel
#hozzá) Ha nincs ilyen nevű szerver, akkor írd ki, hogy nincs ilyen szerver!
talalat = False

f_szerver = input("Írd be egy szerver nevét: ")
for szerver in szerverek:
    if szerver['nev'] == f_szerver:
        talalat = True
        print(f"Ezen a szerveren a VIP csomag ára {vip_ar(szerver['havi_dij'])} Ft lenne.")

if not talalat:
    print("Nincs ilyen szerver!")

#5. Írd ki a minecraft-export.txt fájlba a survival módú szerverek neveit!
path = os.path.join(os.path.dirname(__file__), "minecraft-export.txt")

with open(path, "w", encoding="utf-8") as f:
    for szerver in szerverek:
        if szerver['mod'] == 'survival':
            f.write(szerver['nev'])
            f.write('\n')