
szo1 = input("Írj egy szót! ")
szo2 = input("Írj egy szót! ")
szo1_van = szo1.find("e")
szo2_van = szo2.find("e")
if szo1_van >0 and szo2_van > 0:
    print("Vann bennük e.")
else:
    print("Nincs!")
