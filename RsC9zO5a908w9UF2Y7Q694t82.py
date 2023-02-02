neve = input("Adja meg a fájl nevét! ")
if (neve != ""):
    file = open(f"./{neve}.txt","w")
    print(f"./{neve}.txt")
    i = 0
    while True:
        line = input(f"Szöveg írása a ({i}. sorba) ")
        if (line != "stop"):
            file.write(f"{line}\n")
        else:
            file.close()
            break
        i += 1
else:
    print(f"A fájl név ({neve}) nem elfogadható!!")
