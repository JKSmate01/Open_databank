class Allat:
    def __init__(self,nev,mass):
        self.mass = mass
        self.nev = nev
w = open("./legnehezebb.txt","w")
allatok = []
for _ in range(3):
    neve = input("Add meg egy állatfaj nevét! ")
    tomgege = int(input("Hány kilogramm a tömege egy példánynak? "))
    allat = Allat(neve,tomgege)
    allatok.append(allat)
max = allatok[0].mass
w.write(f"A(z) {allatok[0].nev} a legnagyobb tömegű ({allatok[0].mass}kg).")
for allat in allatok:
    print(f"A(z) {allat.nev} tömege {allat.mass}kg.")
    if (allat.mass > max):
        max = allat.mass
        w.write(f"A(z) {allat.nev} a legnagyobb tömegű ({allat.mass}kg).")
w.close()

