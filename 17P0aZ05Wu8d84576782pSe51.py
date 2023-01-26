
def szor():
    szorzando = 5
    szorzo = input("Mennyivel szorozza meg az " + str(szorzando) + "-öt? ")
    print(szorzando, " ször ", szorzo, " annyi mint ",sep="",end="")
    szorzo =int(szorzo)
    print(szorzando*szorzo)
def el():
    ellenség = input("Ki volt a Piroska nevű szuperhős főellensége? ")
    if (ellenség == "farkas" or ellenség == "Farkas"):
        print("Okos vagy")
        print("Nem is kicsit....")
    elif (ellenség == "ordas" or ellenség == "Ordas"):
        pass
        #print("Háááát...nem egészen.")
    else:
        print("Háááát.....")
        print("Nem.")
    print("Legközelebb a hét törpét kérdezem - visszafelé!")

def w():
    osszeg = None
    while osszeg != 4:
        osszeg = input("Mennyi kétszer kettő? ")
        osszeg = int(osszeg)
    print("Annyi!")
def f():
    varosok = ["Miskolc","Párizs","Dublin","Lajosmizse"]
    for index, varos in enumerate(varosok):
        print(index+1, varos, "egy város Európában")
