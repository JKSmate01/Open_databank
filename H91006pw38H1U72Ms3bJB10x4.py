old1 = int(input("Adja meg az egyik könyv oldalszámát: "))
old2 = int(input("Adja meg a másik könyv oldalszámát: "))

if old1 > old2:
    print(f"Az első nagyobb mint a másik")
elif old1 == old2:
    print(f"Egyenlően hosszúak")
else:
    print(f"A másik nagyobb mint az első")
