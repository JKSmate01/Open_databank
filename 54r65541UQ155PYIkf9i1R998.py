
def check(m):
    if (m >= 170):
        return True
    else:
        return False

while True:
    nev = input("Add meg a jelentkező nevét! ")
    if (nev == ""):
        break
    magassag = int(input("Hány centiméter magas? "))
    check(magassag)
    if (check(magassag)):
        print(f"{nev} megfelelő magasságú.")
    else:
        print(f"{nev} nem megfelelő magasságú.")
