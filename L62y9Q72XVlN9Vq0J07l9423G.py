import math
import random
v = input("")
if (v == "r"):
    m = int(random.randint(1, 10))
    r = int(random.randint(1, 10))
    print(f"m = {m} r = {r}")
else:
    m = float(input("Magassága (m)? (méterben) "))
    r = float(input("Kör sugara (r)? (méterben) "))
V = (r**2) * math.pi * m
print(f"Térfogata: {(V):2.2f} m3")
Ta = math.pi * (r**2)
Tp = 2 * math.pi * r * m 
T = Ta+Tp
print(f"Az alap területe: {(Ta):2.2f} m2 és a palást területe: {(Tp):2.2f} m2")
