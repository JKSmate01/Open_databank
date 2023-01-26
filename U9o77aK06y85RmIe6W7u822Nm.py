import random
hatosak = 0
for _ in range(1000000):
    dob = random.randint(1,6)
    if (dob == 6):
        hatosak += 1
print(hatosak)
