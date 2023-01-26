#25000ft
#gép típusa,
#működik-e
#ára
#input megvesszük-e

def mine():
    G_l = [] #megvett gépek
    p = 25000 #pénzünk

    while p > 0:
        if (len(G_l) > 0):
            print("Gépeink:")
            for index, gepek in enumerate(G_l):
                print(index+1, gepek)
        t = input("Adja meg a gép típusát! ")
        m = input("Működik a gép? ")
        if (m == "Igen" or m == "igen" or m == "y"):
            ar = int(input("Mennyibe kerül? "))
            print(f"Összesen eddig {p}Ft-unk van.")
            if (p >= ar):
                p -= ar
                G_l.append(t)
                print(f"Megvétele után {p}Ft-unk lett.")
            else:
                print("Nincs elég pénzed hozzá!")
                break
        elif(m == "Nem" or m == "nem" or m == "no"):
            print("Akkor nem vesszük meg! ")


#Tanárúré
def t():
    név = input("Mi a gép neve? ")
    működik = True if input("Működik (i/n)? ") == "i" else False
    ár = int(input("Mi az ára? "))

    if (név == "ZX Spectrum" or név == "C64") and működik and ár <= 25000:
        print("Biznisz!!!")
    else:
        print("Gagyi nyolcbitesek... Kinek kellenek?!")
t()