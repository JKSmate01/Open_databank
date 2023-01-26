import math
def orai():
    a = int(input("Írj egy számot "))
    b = int(input("Írj egy másik számot "))
    c = a+b

    print(a)
    print(b)
    print(a+b)
    print(c)
    print(f"Az {a} és {b} öszzege = {c}-vel egyenlő")

    if a > b:
        print(f"{a} nagyobb mint {b}")
    elif b > a:
        print(f"{b} nagyobb mint {a}")
    elif a == b:
        print(f"{a} és {b} egyenlőek")

    if a % 2 == 0:
        print(f"{a} páros!")
    else:
        print(f"{a} páratlan!")

'''
Feladat
k. 3 szám, háromszög oladai.
számolja ki T és K.
'''
def feladat():
    a = int(input("Add meg az a oldal hosszát!"))
    b = int(input("Add meg a b oldal hosszát!"))
    c = int(input("Add meg a c oldal hosszát!"))
    K = a+b+c
    s = K/2
    T = s*math.sqrt(s-a)*(s-b)*(s-c)
    print(f"A háromszög területe: {T} és kerülete: {K}")
    
print("0: orai, 1:feladat")
ch = int(input())
if (ch == 0):
    orai()
elif (ch == 1):
    feladat()
