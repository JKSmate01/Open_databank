wr = open("H:\ev.txt","w")

ev = [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650,]
ev_b = False
wr.write(f"{ev}\n")
wr.write(f"{ev_b}\n")
if (len(ev) == 12):
    ev_b = True
    print(f"ez egy év adatsora")
    wr.write(f"ez egy év adatsora\n")
else:
    print(f"ez nem egy év adatsora!")
    wr.write(f"ez nem egy év adatsora!\n")
ln = ev[0]
for szam in ev:
    if szam > ln:
        ln = szam
print(f"A legnagyobb: {ln}")
wr.write(f"A legnagyobb: {ln}\n")
lk = ev[0]
for szam in ev:
    if szam < lk:
        lk = szam
print(f"A legkisebb: {lk}")
wr.write(f"A legkisebb: {lk}\n")
ossz = 0
for szam in ev:
    ossz += szam
print(f"Összesen: {ossz}")
wr.write(f"Összesen: {ossz}\n")
#2400 alatt
ker = 2400
menny = 0
for szam in ev:
    if (szam < 2400):
        menny += 1
print(f"{menny} hónapban volt 2400 alatt.\n")
wr.write(f"{menny} hónapban volt 2400 alatt.\n")
i = 0
while i < len(ev) and ev[i] != ln:
    i+=1
print(f"A legnagyobb a(z) {i+1}. helyen van!")
wr.write(f"A legnagyobb a(z) {i+1}. helyen van!\n")
i = 0
while i < len(ev) and ev[i] != lk:
    i+=1
print(f"A legkisebb a(z) {i+1}. helyen van!")
wr.write(f"A legkisebb a(z) {i+1}. helyen van!\n")
wr.close()
