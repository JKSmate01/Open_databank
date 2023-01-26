import random
fvarosok = ["Bécs","Bern","Párizs","London","Budapest","Varsó","Prága","Róma","Madrid","Helsinki","Moszkva"]
fvaros = None
while fvaros != "":
    print("fvárosok jelenleg:",",".join(fvarosok))
    fvaros = input("Kérek egy fvárost! ")
    if (fvaros != ""):
        fvarosok.append(fvaros)
for index, fovaros in enumerate(fvarosok):
    print(index, fovaros)
n = random.randint(0, len(fvarosok))
print("A számítógép szerint ez a főváros a legszebb:", fvarosok[n])
while len(fvarosok) > 0:
    print("fovarosaink:",",".join(fvarosok))
    melyik = input("Melyik főváros a legszebb, válaszd ki! ")
    if melyik in fvarosok:
        fvarosok.remove(melyik)
    else:
        print("Ilyen város nincs a listában!")
