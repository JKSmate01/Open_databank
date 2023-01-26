import math
ps=[10,20,30,40]
qs=["cs","e","b"]
print(ps,qs)

#beágyazott
zs = ["hello",2.0,5,[10,20]]
print(zs)
print(zs[3])
szotar=["a","s","k"]
szamok = [17, 123]
ures_lista = []
print(szotar, szamok, ures_lista)

#Elemek elérése
szamok = [17,123]
#elemek helye
print(szamok[0])
for i in enumerate(szamok):
    print(i)

# mit csinálunk?
for (i,ert) in enumerate(szamok):
    szamok[i] = math.pow(ert,2)
    print(szamok[i])
for (i,v) in enumerate(["b","a","k","c"]):
    print(i,v)

#lista metódusok
s = []
s.append(6)
s.append(20)
s.append(4)
s.append(16)
print(s)
# Szúrjuk be a 10-t az 1-es pozícióra, eltolva a többi elemet!
s.insert(1,10)
print(s)
s.insert(0,16)
print(s)
# Hány 16-os szerepel a listában?
print(s.count(16))
#Lista beszúrása a lista s végére!
s.extend([5,9,5,11])
print(s)
#Keressük meg az első 9-es érték indexét a listában!
print(s.index(9))
#Fordítsuk meg a listát!
s.reverse()
print(s)

# Rendezzük a listát növekvőbe!
s.sort()
print(s)
#Távolítsuk el az első 12-es értéket!
s.remove(12)
print(s)
#Rendezzünk egy szöveges adatokat tartalmazó listát!
sz=["b","a","m"]
sz.sort()
print(s)
sz2 = ["én","te","ő","mi","ti","ők"]
sz2.sort()
print(sz2)