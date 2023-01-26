neved = input("Neved: ")
for index in range(1,101):
    print(index,neved,end=",")
print("")
menny = 1
while menny < 101:
    print(menny,neved,end=",")
    menny += 1
print("")
print(neved * 100)

