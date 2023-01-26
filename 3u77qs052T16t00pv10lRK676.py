
print(chr(97)) #Ki íratjuk a 97-es karaktert ami "a"
for d in range(1,800):
    print(chr(d),ord(chr(d)),end=",")
print("")
szov = input("Írjbe egy szöveget! ")
print(f"A {szov}, {len(szov)} karakterből áll.")
for a in range(len(szov)):
    print(f"szov[{a}]: {szov[a]}",end=", ") 
print("")
for g in range(1,len(szov)+1):
    print(f"{szov[-g]}",end="") #Visszafelé kiíratja
print("")
print(szov[2:4]) #A másodiktól a negyedikig ki íratja a szöveget
print("A szöveg id formában: ",id(szov))
tomb = input("Írjon egy sor szöveget ':'-tal elválasztva. ")
tm = tomb.split(":")
print(tm)
e,m,h = tomb.split(":")
print(e,m,h)
szov2 = input("Írj egy szöveget amiben szerepel a kacsa szó! ")
if ("kacsa" in szov2):
    print("Benne van!")
else:
    print("Nincs benne!")
szoveg = '6'
print(szoveg.isdigit()) #Szám?
print(szoveg.isalnum()) #Csak számok és betűk?
print(szoveg.isalpha()) #Csak betűk?
print(szoveg.islower()) #Csak kisbetűs?
print(szoveg.isupper()) #Csak nagybetűs?
print(szoveg.istitle()) #Cím? Vagyis minden szó nagybetűvel kezdődik?
print(szoveg.isspace()) #Whitespace karakterek?
print(szoveg.isprintable()) #Nyomtatható karakterek:
lista1 = ['a', 'b', 'c']
str1 = ''.join(lista1)
str2 = ':'.join(lista1)
print(str1)
print(str2)
#Első betű nagybetű:
szoveg="adwadw"
print(szoveg.capitalize())
#Minden kisbetűs:

print(szoveg.lower())
#Minden nagybetűs:

print(szoveg.upper())
#Minden szó első betűje nagybetű:

print(szoveg.title())
#A nagy volt legyen kicsi, ami kicsi volt legyen nagy:

print(szoveg.swapcase())
for i in range(1,100,2):
    print(i)

for i in range(100,1,-2):
    print(i)

ip=input("IP cím: ")
ipds = ip.replace(".","")
print(ipds)