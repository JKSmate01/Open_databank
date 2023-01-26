from operator import ne


for i in range(1, 100):
    print(i,end=",")
print("")
for u in range(1, 100, 2):
    print(u,end=",")
print("")
for d in range(100, 1, -1):
    print(d,end=",")
print("")
inp = int(input("Írjon be egy számot!"))
for index in range(0, inp):
    print(index+1, end=" , ")
print("")
for ind in range(inp, 0,-1):
    print(ind, end=" , ")
menny = int(input("Hány számot akarsz összeadni? "))
szamok = []
for _ in range(0,menny):
    szam = int(input("Írj egy számot! "))
    szamok.append(szam)
    for szam in szamok:
        print(szam,end="+")
ossz = 0
for szam in szamok:
    ossz += szam
print(f"={ossz}")
nev = input("Írj egy nevet! ")
print(len(nev))
print(nev[0])
for n in range(len(nev)):
    print(ord(nev[n]), chr(ord(nev[n])))
print(nev[:2])