
def mine():
    elfogyasztott = 0
    while (elfogyasztott/10) < 3.5:
        adag = float(input("Mennyi vizet ittál(dl)? "))
        if (adag > 0):
            elfogyasztott += adag
            print(f"Eddig {elfogyasztott} dl vizet ittál ({elfogyasztott/10} l).")
            if (elfogyasztott/10) >= 2.5 and (elfogyasztott/10) < 3:
                print("Elérted a 2.5 l vizet!")
        else:
            print(f"Összesen {elfogyasztott/10} l vizet ittál!")
            break
    if ((elfogyasztott/10) >= 3.5):
        print(f"Gratulálok meg ittál 3.5 l vizet ({elfogyasztott/10} l). Viszlát!")
def tu():
    ossz = 0
    while ossz <= 35 and (ivas := float(input("Hány decit ittál? "))):
        print(f"Már {(ossz:=ossz+ivas)/10:3.1f} litert ittál.")
        if (ossz >= 25):
            print("Már sikerült elérned a 2,5 litert.")
    print("Béka nől a hasadba!")
tu()