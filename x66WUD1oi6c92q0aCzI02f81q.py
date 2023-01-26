print("1.")
for i in range(50):
    for d in range(50):
        print(".",end="")
    print("")
print("2.")
pont = 1
for i in range(50):
    for d in range(pont):
        print(".",end="")
    print("")
    pont+=1
print("3.")
pont=50
for i in range(50):
    for d in range(pont):
        print(".",end="")
    print("")
    pont-=1
print("4.")
for i in range(50):
    print("")
    for d in range(25):
        print("BW",end="")
    print("")
print("5.")