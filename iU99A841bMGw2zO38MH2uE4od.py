#három szám bekérése
#a konstans
#b random (5-25)
#c felhasználó adja meg
#vizsgálat:
#b páros-e
#c páratlan-e
import random
A = 23 
b = random.randint(5,25)
c = int(input("Adj meg egy számot! "))
l = [A,b,c]
if not(b%2):
    print(f"A b páros! ({b})")
elif (b%2):
    print(f"A b páratlan! ({b})")
if (c%2):
    print(f"A c páratlan! ({c})")
elif not(c%2):
    print(f"A c páros! ({c})")
d = A * b * c
print(d)
if (d > 500):
    print("Nagyobb 500-nál!")
else:
    print("Nem nagyobb!")
n = []
print("Csökkenő: ", end="")
while len(l) > 0:
    leg = 0
    for i in range(len(l)):
        if (l[i] > leg):
            leg = l[i]
    print(leg, end=",")
    n.append(leg)
    l.remove(leg)
print(" ")
print("Növekvő: ", end="")
for d in range(len(n)):
    print(n[len(n)-1], end=",")
    n.remove(n[len(n)-1])
