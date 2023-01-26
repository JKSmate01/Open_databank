import math
m = float(input("Adja meg a testtömegét (kg) "))
h = float(input("Adja meg a magasságát (m)"))
e = m / math.pow(h,2)
print(e)
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