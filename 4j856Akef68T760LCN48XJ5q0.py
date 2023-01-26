
lin = False

while not lin:
    username = input("Kérem adja meg a felhasználónevét! ")
    passowrd = input("Kérem adja meg a jelszavát! ")
    if (username == "bori99" and passowrd == "kismehe<3"):
        print("a belépés megengedve!")
        lin=True
    else:
        print("belépés megtagadva!")
