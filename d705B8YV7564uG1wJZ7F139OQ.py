import random
print("1.")
for i in range(1,11):
    if i % 2 == 0:
        print(i,end=",")
print("")
print("2.")
d = []
for i in range(1,11):
    if i % 2 == 0:
        d.append(i)
d.reverse()
for e in range(len(d)):
    print(d[e],end=",")
print("")
print("3.")
for i in range(1,11):
    if i % 2 != 0:
        print(i,end=",")
print("4.")
alkalom = int(input("Hányszor akarja kiíratni? "))
szov = input("Milyen szöveget akar kiíratni? ")
if (alkalom >0):
    for i in range(alkalom):
        print(szov)
print("5.")
paros = int(input("Írjon be egy páros számot. "))
while paros % 2 != 0:
    paros = int(input("Írjon be egy páros számot. "))
print(f"Ok, a {paros} tényleg páros szám!")