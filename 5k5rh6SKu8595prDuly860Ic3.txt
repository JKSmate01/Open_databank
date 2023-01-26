def nagysag(letszam):
    if (letszam >= 1000):
        return True
    else:
        return False
while True:
    neve = input("Add meg az iskola nevét! ")
    if (neve == ""):
        break
    letszam = int(input("Add meg a pontszámát! "))
    if (nagysag(letszam)):
        print(f"{neve} nagy létszámú iskola.")
    else:
        print(f"{neve} kis létszámú iskola.")
