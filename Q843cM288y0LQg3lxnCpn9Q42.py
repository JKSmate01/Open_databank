psw = ["bori99","Szivecske<3"]
while True:
    name = input("Adja meg a felhasználónevét! ")
    password = input("Adja meg a jelszavát! ")
    if (name == psw[0] and password == psw[1]):
        print("Belépés engedélyezve.")
        break
    else:
        print("Belépés megtagadva.")
