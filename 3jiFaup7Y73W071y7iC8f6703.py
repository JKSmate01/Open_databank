import math
a = float(input("Kérem a másodfokú egyenlet főegyütthatóját: "))
while a==0:
    print("Ez nem lesz másodfokú egyenlet, nem oldom meg.")
    a = float(input("Kérem a másodfokú egyenlet főegyütthatóját: "))

b = float(input("Kérem az elsőfokú tag együtthatóját: "))
c = float(input("Kérem a konstans tagot: "))
d = (b**2)-4*a*c
print(f"A diszkrimináns értéke: {d}")

if d>=0:
    print("Van valós megoldás.")
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print("Az egyik megoldás", x1)
    print("A másik megoldás", x2)