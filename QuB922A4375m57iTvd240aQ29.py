szam1 = int(input("Adj meg az egyik iskolai számot! "))
szam2 = int(input("Adjon meg egy másik iskolai számot! "))
if (szam1 > szam2):
    print(f"A létszám érték az egyik iskolában több, {szam1}")
elif (szam1 < szam2):
    print(f"A létszám érték a másik iskolában több, {szam2}")
else:
    print("A két létszám egyenlő")


