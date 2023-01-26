#bekér név pont
#átmegy 48 or higher
def eldont(pt):
    if (pt >= 48):
        return True
    else:
        return False
wr = open("H:\ki.txt","w")
while True:
    nev = input("Add meg a vizsgázó nevét! ")
    if (nev != ""):
        wr.write(f"Add meg a vizsgázó nevét! {nev}\n")
        pont = int(input("Add meg a pontszámát! "))
        wr.write(f"Add meg a pontszámát! {pont}\n")
        if (eldont(pont) == True):
            print(f"{nev} vizsgája sikeres.")
            wr.write(f"{nev} vizsgája sikeres.\n")
        else:
            print(f"{nev} vizsgája sikertelen.")
            wr.write(f"{nev} vizsgája sikertelen.\n")
    else:
        break
wr.close()
