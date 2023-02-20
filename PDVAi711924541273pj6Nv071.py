def letszam(num):
    border = 1000
    if (num >= border):
        return True
    else:
        return False
while True:
    nev = input("Iskola neve: ")
    if (nev == ""):
        break
    szam = int(input("Hányan vannak? "))
    if (letszam(szam)):
        print(f"{nev} egy nagyiskola")
    else:
        print(f"{nev} egy kisiskola")




