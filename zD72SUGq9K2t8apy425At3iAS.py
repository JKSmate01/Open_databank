print("1.")
for i in range(1,41):
    if (i % 3 == 0):
        print(i)
print("2.1.")
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
for szo in range(len(szavak)):
    if (szavak[szo][0] == "t" or szavak[szo][0] == "T"):
        print(szavak[szo])
print("2.2.")
t = []
for szo in range(len(szavak)):
    if (szavak[szo][0] == "t" or szavak[szo][0] == "T"):
        t.append(szavak[szo])
print(t)
print("3.")
szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]
for i in range(len(szamok)):
    if (szamok[i] % 3 == 0):
        print(szamok[i])




