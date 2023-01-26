import random as r
#8
wr = open("H:\out.txt","w")
def alahuzas(ilyen):
    print(ilyen)
szam1 = int(input("Adjon meg egy számot! "))
szam2 = r.randint(10,50)
SZAM3 = 40
#2
while szam2 % 2 == 0:
    szam2 = r.randint(10,50)
#3
if (szam1 % 2 == 0):
    alahuzas(f"Első szám: {szam1} (Páros)")
    wr.write(f"Első szám: {szam1} (Páros)\n")
else:
    alahuzas(f"Első szám: {szam1} (Páratlan)")
    wr.write(f"Első szám: {szam1} (Páratlan)\n")
alahuzas(f"Második szám: {szam2}")
wr.write(f"Második szám: {szam2}\n")
alahuzas(f"Harmadik szám: {SZAM3}")
wr.write(f"Harmadik szám: {SZAM3}\n")
szamok = [szam1,szam2,SZAM3]
alahuzas(f"Lista: {szamok}")
wr.write(f"Lista: {szamok}\n")
#4
ossz = 0
for szam in szamok:
    ossz += szam
alahuzas(f"A lista összege: {ossz}")
wr.write(f"A lista összege: {ossz}\n")
ossz = 1
for szam in szamok:
    ossz *= szam
alahuzas(f"A lista szorzata: {ossz}")
wr.write(f"A lista szorzata: {ossz}\n")
alahuzas(f"A lista első ({szamok[0]}) és utolsó ({szamok[len(szamok)-1]}) eleme.")
wr.write(f"A lista első ({szamok[0]}) és utolsó ({szamok[len(szamok)-1]}) eleme.\n")
maxE = szamok[0]
minE = szamok[0]
for szam in szamok:
    if (szam > maxE):
        maxE = szam
for szam in szamok:
    if (szam < minE):
        minE = szam
alahuzas(f"A lista legkisebb ({minE}) és legnagyobb ({maxE}) elemei.")
wr.write(f"A lista legkisebb ({minE}) és legnagyobb ({maxE}) elemei.\n")
szamok_k = szamok.sort()
alahuzas(f"A lista sorban: {szamok_k}")
wr.write(f"A lista sorban: {szamok_k}\n")
szamok_k = szamok.sort(reverse=True)
alahuzas(f"A lista visszafelé: {szamok_k}")
wr.write(f"A lista visszafelé: {szamok_k}\n")
#5
halmaz = set(szamok)
alahuzas(halmaz)
halmaz.add("tt")
alahuzas(halmaz)
halmaz.remove("tt")
alahuzas(halmaz)
halmaz2 = halmaz.copy()
alahuzas(halmaz2)
halmaz2.pop()
alahuzas(halmaz2)
alahuzas(halmaz - halmaz2)
#6
with open("H:\JakusMate.txt","w") as file:
    for i in range(len(szamok)):
        file.write(f"{szamok[i]},")
#7
re = open("H:\JakusMate.txt","r")
alahuzas(re.readline())
wr.write(re.readline())
wr.close()