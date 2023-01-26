import math
ms = []
hs = []
es = 0
for i in range(3):
    ms.append(float(input(f"Adja meg a(z) {i+1}. testtömegét (kg) ")))
    hs.append(float(input(f"Adja meg a(z) {i+1}. magasságát (m)")))
for d in range(len(ms)):
    e = ms[d] / math.pow(hs[d],2)
    es += e
    print(f"{d+1}. Testtömeg indexe: {e:0.2f}")
    if (e < 16):
        print("soványság")
    elif (e > 16 and e < 16.99):
        print("Mérsékelt soványság")
    elif (e > 17 and e < 18.49):
        print("Enyhe soványság")
    elif (e > 18 and e < 25):
        print("Normál")
    elif (e > 26 and e < 30):
        print("Enyhe túlsúly")
    elif (e >= 31):
        print("Elhízott")
print(f"Átlag: {es/3}")
ms.sort()
print("Súlyok ",ms)
hs.sort()
print("Magasságok ",hs)
ms.reverse()
hs.reverse()
print("Súlyok ",ms)
print("Magasságok ",hs)
