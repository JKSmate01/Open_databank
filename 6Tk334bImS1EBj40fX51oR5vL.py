import math
a = float(input("Kérem a másodfokú egyenlet főegyütthatóját: "))
while a==0:
    print("Ez nem lesz másodfokú egyenlet.")
    a = float(input("Kérem a másodfokú egyenlet főegyütthatóját: "))

b = float(input("Kérem az elsőfokú tagot: "))
c = float(input("Kérem a konstans tagot: "))
d = math.pow(b,2)-4*a*c
print(d)

if d>=0:
    print("Van valós megoldás.")
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print("Az egyik megoldás", x1)
    print("A másik megoldás", x2)
