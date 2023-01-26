#Összegzés, szorzás, szöveg összefűzés tétele
t = [3,8,2,4,5,1,6]
t1 = ["d","f","g","h","j","k","u","g"]
osszeg = 0
szorzas = 1
konkat = ""
for num in t:
    osszeg += num
    szorzas *= num
print(f"Összesen: {osszeg}")
print(f"Szorzata: {szorzas}")
for szov in t1:
    konkat += szov
print(f"Szöveg: {konkat}")
#5-nél nagyobb számok megszámlálása t-ben
count = 0
for number in t:
    if number > 5:
        count += 1
print(f"5-nél nagyobb számok száma {count}")
#Eldöntés tétele
hossz = len(t)
ker = 5
i=0
while i < hossz and t[i] != ker:
    i += 1
if i<hossz:
    print(f"Van ilyen: {ker}")
else:
    print("Nincs!")
#Kiválasztás, kiválogatás, szétválogatás
hossz = len(t)
ker = 5
i=0
while t[i] != ker:
    i += 1
print(f"Hanyadik helyen van: {i+1}")
#lineáris
hossz = len(t)
ker = 5
i=0
while i < hossz and t[i] != ker:
    i+=1
    if (i<hossz):
        print(f"van {ker} elem a listában")
        print(f"helye {i+1}")
    else:
        print("Nincs a listában!")
#Szélsőérték (max,min)
maxElem = t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
print(maxElem)
minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)
print(f"Átlag : {(maxElem+minElem)/2}")
#Max kimentése .txt formátumban
wr = open("H:\egyeb\max.txt","w")
maxElem = t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
wr.write(f"Legnagyobb: {maxElem}\n")
print(maxElem)
minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
wr.write(f"Legkisebb: {minElem}\n")
print(minElem)
print(f"Átlag : {(maxElem+minElem)/2}")
wr.write(f"Átlag: {(maxElem+minElem)/2}\n")
wr.close()
#kiválogatás
b=[]
c=[]
d=[]
e=[]
def dupla(num):
    return num*2
for elem in t:
    b.append(dupla(elem))
    if elem%2 == 0: #Ha páros
        c.append(elem)
    if elem%2 != 0:
        e.append(elem)
    if elem <5: #Ha kisebb 5-nél
        d.append(elem)
print(b)
print(c)
print(e)
print(d)

#buborék rendezés
#t = [3,8,2,4,5,1,6]
n = len(t)
for i in range(n-1,0,-1):
    for j in range(0,i):
        if (t[j] > t[j+1]):
            tmp = t[j+1]
            t[j+1] = t[j]
            t[j] = tmp
print(t)
#Fájl írás 2.
with open("H:\egyeb\E.txt","w",encoding = "utf-8")as file:
    file.write("Csordásné Kovács Judit")
