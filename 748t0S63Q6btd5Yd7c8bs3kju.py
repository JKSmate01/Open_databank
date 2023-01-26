
celsius = float(input("Adja meg a hőmérsékeltet Celsius fokban: "))
kelvin = celsius + 273.15
print(f"A megadott hőmérséklet Kelvin-ben: {kelvin}")
if (celsius < 4):
    print("Hideg")
elif (celsius >= 5 and celsius <= 24):
    print("Elviselhető")
elif (celsius >= 25):
    print("Hőség")