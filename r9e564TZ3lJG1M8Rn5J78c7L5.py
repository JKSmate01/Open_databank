import random
def szoveges():
    fd = []

    for _ in range(10):
        f = random.choice(["f","í"])
        fd.append(f)
    print("A feldobások:",", ".join(fd))

    fuf = 0 #fej után fej

    for index, f in enumerate(fd):
        if (index > 0 and f == "f" and fd[index-1]=="f"):
            fuf += 1
    print("Ennyiszer volt fej után fej: ",fuf)
def szamos():
    dobasok = []
    for _ in range(10):
        dobas = random.randint(0,1)
        dobasok.append(dobas)
    print("A feldobások:",",".join(dobasok))

def szamos_egy():
    dobas = random.randint(0,1)
    if dobas == 0:
        print("Fej")
    else:
        print("Írás")
def szoveges_egy():
    dobas = random.choice(["F","Í"])
    print(dobas)
szoveges_egy()
#szamos_egy()