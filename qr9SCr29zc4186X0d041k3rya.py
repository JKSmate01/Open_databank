import random as r
wr = open("H:\\fa.txt","w")
def iras(szoveg):
    print(szoveg)
    wr.write(szoveg)
okt = []
for i in range(31):
    okt.append(r.randint(50,100))
iras(f"{okt}\n")
#2&3
maxfa = okt[0]
minfa = okt[0]
for nap in okt:
    if (nap > maxfa):
        maxfa = nap
    if (nap < minfa):
        minfa = nap
iras(f"Legtöbb kitermelt: {maxfa} és a legkevesebb: {minfa}\n")
#4
count = 0
for nap in okt:
    if (nap > 82):
        count += 1
iras(f"{count} alkalommal volt 82 m3 felett.\n")
#5
mikor = 20
iras(f"Október 20.-án {okt[mikor-1]}db volt.\n")
#6
atlag = 0
for nap in okt:
    atlag += nap
iras(f"Októberben az átlag: {atlag/len(okt):0.2f} volt\n")
wr.close()