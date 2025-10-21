# Számrendszerek
binary = bin(90)
print(binary) # 0b1011010 (0b jelezi, hogy ez egy binéris)
print(type(binary)) # string
print("0b nélkül: ", binary[2:]) # 0b nélkül

hexa = hex(4219)
print(hexa)
print(type(hexa)) # string

# Hol használjuk a 16-os számrendszert?
# RGB kódok színeknél  #FF1010 vörös szín (255 piros, 16 zöld, 16 kék)
# MAC címeknél
# IPv6-os ip címek (f)

class Valami:
    pass

var = Valami()
print(var)

octa = oct(90)
print(octa)

binary = "10110101011"
num = int(binary) #alapesetben az int() fgv. 10-es számrednszerű számként értelmezi
print(num)
num = int(binary, 2)
print(num)

hexa = "3CF2"
num = int(hexa, 16)
print(num) #15602

# Mi van ha 16-ból akarunk 2-be?
binary = bin(int(hexa, 16))
print(binary) # 0b11110011110010


# Bináris operátorok

num1 = 42
num2 = 97

print(num1 & num2)
print(num1 | num2)
print(num1 ^ num2)

num = 42

print(num >> 1) # 21
print(num >> 2) # 10
print(num >> 3) # 5

print(num << 1) # 84
print(num << 2) # 168
print(num << 3) # 336

# Határozzuk meg, hogy x GigaByte az TeraByte, MegaByte, KiloByte, Byte, bit
# 1 TB = 1024 GB
# 1 GB = 1024 MB
# 1 MB = 1024 KB
# 1 KB = 1024 B
# 1 B = 8 bit
# 1 bit = 1 db 1-es vagy 0-s

giga = int(input("Add meg a GigaByte-ok számát:"))
print(f"Ez {giga/1024} Terabyte")
print(f"Ez {giga << 10} MegaByte")
print(f"Ez {giga << 20} KiloByte")
print(f"Ez {giga << 30} Byte")
print(f"Ez {giga << 33} Bit")

