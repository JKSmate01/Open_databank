def szarmazas(kod):
    hazai = 599
    if (kod == hazai):
        return True
    else:
        return False
while True:
    neve = input("Add meg a vásárló nevét! ")
    if (neve == ""):
        break
    vonalkod = int(input("Add meg a gyümölcs vonalkódjának első három számát ! "))
    if (szarmazas(vonalkod)):
        nemzet = "magyar"
    else:
        nemzet = "nem magyar"
    print(f"{neve} {nemzet} gyümölcsöt vásárolt.")
