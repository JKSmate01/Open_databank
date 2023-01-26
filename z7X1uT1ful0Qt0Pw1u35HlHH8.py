
liba = [2,4,7,9,8,5,4,3]
ossz = 0
for i in range(len(liba)):
    ossz += liba[i]
print(f"Össz súly: {ossz}kg")
print(f"{len(liba)}db")
atlag = ossz / len(liba)
print(f"Az átlag súly: {atlag}kg")
nehezebb = []
ossz_n = 0
for i in range(len(liba)):
    if (liba[i] >= 5):
        nehezebb.append(liba[i])
for i in range(len(nehezebb)):
    ossz_n += nehezebb[i]
    liba.remove(nehezebb[i])
print(f"A róka {len(nehezebb)}db libát visz el ({ossz_n}kg)")
print(liba)
liba2 = [4,7,8,6,5,3]
for d in range(len(liba)):
    liba.append(liba2[d])
print("Új libák: ",liba)
ossz = 0
for i in range(len(liba)):
    ossz += liba[i]
print(f"Össz súly: {ossz}kg")
print(f"{len(liba)}db")
atlag = ossz / len(liba)
print(f"Az átlag súly: {atlag}kg")
nehezebb = []
ossz_n = 0
for i in range(len(liba)):
    if (liba[i] >= 5):
        nehezebb.append(liba[i])
for i in range(len(nehezebb)):
    ossz_n += nehezebb[i]
    liba.remove(nehezebb[i])
print(f"A róka {len(nehezebb)}db libát visz el ({ossz_n}kg)")
print(liba)
liba3 = ["fekete liba","tarka liba"]