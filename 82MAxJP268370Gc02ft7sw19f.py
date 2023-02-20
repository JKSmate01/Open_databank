#ügyes gyűjtő 800000
def eldont(menny):
    if (menny >= 800000):
        return True
    else:
        return False

while True:
    neve = input("Add meg az könyvtár nevét!")
    if (neve == ""):
        break
    menny = int(input("Add meg a gyűjtött kötetek mennyiségét (ezer)!"))
    if (eldont(menny*1000)):
        print(f"{neve} ügyes gyűjtő címet kap.")
    else:
        print(f"{neve} kevésbé szorgalmas címet kap.")


