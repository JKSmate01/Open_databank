#min 150
#170 felett felsőfokú
#150 és 170 között középfok
def check(p):
    if (p > 150 and p < 170):
        return True
    else:
        return False
while True:
    nev = input("Add meg a vizsgázó nevét! ")
    if (nev == ""):
        break
    pont = int(input("Hány pontja lett? "))
    check(pont)
    if (check(pont)):
        print(f"{nev} vizsga szintje középfokú.")
    else:
        print(f"{nev} vizsga szintje nem középfokú.")

