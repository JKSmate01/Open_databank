t = [1,2,3]
s = set()
s = set(t)
print(s)
with open("H:\Feladatok\egyeb\gyak.txt","w",encoding="utf-8") as file:
    file.write(f"{s}\n")
wr = open("H:\Feladatok\egyeb\gyak.txt","w")
wr.write(f"{s}\n")
d = {6,"ed",8,3,2}
print(d)
wr.write(f"{d}\n")
print(s&d)
wr.write(f"{s&d}\n")
print(d-s)
wr.write(f"{d-s}\n")
print(d|s)
wr.write(f"{d|s}\n")
wr.close()
