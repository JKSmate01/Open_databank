import math
m = float(input("Írja be a magasságot (m) "))
d = float(input("Írja be az átmérőt (m) "))
r = d/2
a = float(math.pow(r,2)+math.pow(m,2))
s = math.sqrt(a)
V = (1/3)*math.pi*math.pow(r,2)*m
Ta = math.pi * math.pow(r,2)
Tp = math.pi * r * s
F = Ta + Tp
print(f"A kúp térfogata: {V:2.2f}m3")
print(f"A kúp felszíne: {F:2.2f}m2")
