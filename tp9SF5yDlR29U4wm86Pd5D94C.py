
def feladat01():
    nev = input("Adja meg a nevét! ")
    print(nev)
    ÉV = 2022
    udv = (f"Üdvözöllek {nev}")
    print(udv,"szép napot kívánok neked", sep = " ")
    eletkor = int(input("kérem adja meg a születési évét "))
    eletk = ÉV - eletkor
    print(eletk)
    if (eletk >= 3 and eletk < 7):
        print("Óvoda")
    elif (eletk >= 7 and eletk <= 14):
        print("Általános")
    elif (eletk > 14 and eletk <= 18):
        print("Közép")
    elif (eletk > 18):
        print("Felnőtt")

def feladat02():
    adatok = []
    adatok.append(input("Kérném a nevét! "))
    adatok.append(input(f"Kérném a(z) {adatok[0]} márkáját! "))
    adatok.append(input(f"Kérném a(z) {adatok[0]} gyártási országát! "))
    adatok.append(int(input(f"Kérném a(z) {adatok[0]} végsebességét! ")))
    print(adatok[2] + " vidékein készült a " + adatok[0] + ", ami " + str(adatok[3]) + " km/h végsebességű!")
    mond = "{} vidékein készült a {}, ami {} km/h végsebességű!".format(adatok[2],adatok[0],adatok[3])
    mond1 = "{0} vidékein készült a {1}, ami {2} km/h végsebességű!".format(adatok[2],adatok[0],adatok[3])
    mond2 = "{1} vidékein készült a {0}, ami {2} km/h végsebességű!".format(adatok[0],adatok[2],adatok[3])
    mond3 = "{o} vidékein készült a {a}, ami {v} km/h végsebességű!".format(o=adatok[2],a=adatok[0],v=adatok[3])
    print(mond)
    print(mond1)
    print(mond2)
    print(mond3)
    print(f"{adatok[2]=}, {adatok[0]=}, {adatok[3]=}")

def feladat03():
    NÉMET = 19
    BRIT = 20
    CSEH = 21
    LENGYEL = 23
    MAGYAR = 27
    
    netto_ar = float(input("Mütyürke ára? "))
    print(f"A mütyürke árai:")
    print(f"{netto_ar*(1+NÉMET/100):10.2f} picula Németországban.")
    print(f"{netto_ar*(1+BRIT/100):10.2f} picula Britanniában.")
    print(f"{netto_ar*(1+CSEH/100):10.2f} picula Cseh.")
    print(f"{netto_ar*(1+LENGYEL/100):10.2f} picula Lengyel.")
    print(f"{netto_ar*(1+MAGYAR/100):10.2f} picula Magyar.")

def feladat04():
    hofok = float(input("Kérem adja meg a hőfokot! "))
    P = 105
    FE_OP = 1539
    FE_FP = 2750

    if (hofok <  FE_OP):
        print("szilárd")
    elif(hofok < FE_FP):
        print("Folyékony")
    else:
        print("Gáz")
    # if (hofok >= FE_OP):
    #     if (hofok >= FE_FP):
    #         print("Folyékony!")
    #     else:
    #         print("Szilárd, de olvadt!")
    # elif (hofok < FE_OP):
    #     print("Szilárd")