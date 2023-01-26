wr = open("H:\\aug.txt","w")
aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]
wr.write(f"{aug}\n")
print(len(aug))
wr.write(f"{len(aug)}\n")
if (len(aug) == 31):
    print("Lehet havi hőmérséklet!")
    wr.write("Lehet havi hőmérséklet!\n")
else:
    print("Nem lehet!")
    wr.write("Nem lehet!\n")
ln = aug[0]
lk = aug[0]
count = 0
for h in aug:
    if (h > ln):
        ln = h
    if (h < lk):
        lk = h
    if (h > 31):
        count += 1
print(f"Legnagyobb: {ln}")
wr.write(f"Legnagyobb: {ln}\n")
print(f"Legkisebb: {lk}")
wr.write(f"Legkisebb: {lk}\n")
print(f"{count} alkalommal volt 31 fok felett.")
wr.write(f"{count} alkalommal volt 31 fok felett.\n")
print(f"Augusztus 20.-án {aug[21]} fok volt")
wr.write(f"Augusztus 20.-án {aug[21]} fok volt\n")
atlag = 0
for i in aug:
    atlag += i
atlag /= len(aug)
print(f"Az átlag hőmérséklet: {atlag:0.2f} fok")
wr.write(f"Az átlag hőmérséklet: {atlag:0.2f} fok\n")
print(f"A hőingadozás: {ln-lk} fok")
wr.write(f"A hőingadozás: {ln-lk} fok\n")
