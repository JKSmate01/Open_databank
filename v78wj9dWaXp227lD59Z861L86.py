#50m
#elég-e ha nem mennyit 
def check(sz,h):
    kell = sz*h
    print(f"A kert bekerítéséhez {kell} méter drótháló kell. ")
    if (kell-50 > 0):
        print(f"Venni kell még {kell-50} métert.")
    else:
        print(f"Ki fog maradni {abs(kell-50)} métert.")
while True:
    hossz = int(input("Milyen hosszú a kert? "))
    if (hossz <= 0):
        break
    szelesseg = int(input("Milyen széles a kert? "))
    check(szelesseg, hossz)

