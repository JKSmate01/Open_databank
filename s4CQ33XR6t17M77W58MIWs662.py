def alahuzas(hossz):
    for _ in range(hossz):
        print(".",end="")
print("Ez egy fontos figyelmeztetés")
alahuzas(len("Ez egy fontos figyelmeztetés"))
print("")
print("Minden sora nagyon fontos!!")
alahuzas(len("Minden sora nagyon fontos!!"))
print("")
def plus(num):
    print(num+2)
szam = int(input("Szám"))
plus(szam)
def plusz(num):
    return(num+2)
print(plusz(3))