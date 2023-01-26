ora = int(input("Hány óra van most? "))
if ora >= 8 and ora < 16:
    print("A bolt nyitva van!")
    mevny=16-ora
    print(f"A bolt még {mevny} órát nyitva van!")
else:
    print("Nem vagyunk nyitva!")
    if (ora > 0 and ora < 8 and ora < 24):
        print(f"A bolt {8-ora} óra mulva fog nyitni!")
    elif (ora > 16 and ora <= 24):
        print(f"A bolt {24-ora} óra mulva fog nyitni!")