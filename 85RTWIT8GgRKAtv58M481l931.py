#páros = jobb
def hol(szam):
    if (szam % 2 == 0):
        return True
    else:
        return False


while True:
    neve = input("Adja meg az utca nevét! ")
    if (neve == ""):
        break
    szam = int(input("Adja meg a ház számát! "))
    if (hol(szam)):
        print(f"A ház a(z) {neve} utca jobb oldalán található.")
    else:
        print(f"A ház a(z) {neve} utca bal oldalán található.")


