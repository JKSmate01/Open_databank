class Egyetem:
    def __init__(self,nev,varos,nemzetiseg):
        self.nev = nev
        self.varos = varos
        self.nemzetiseg = nemzetiseg
    def elotag(self):
        if (self.nemzetiseg == "a"):
            return "angol"
        elif (self.nemzetiseg == "n"):
            return "német"
egyetemek = []
for _ in range(3):
    nev = input("Név: ")
    varos = input("Varos: ")
    nemzet = input("Nemzetiség(a/n): ")
    egyetemek.append(Egyetem(nev,varos,nemzet))
for egyetem in egyetemek:
    print(f"{egyetem.nev} egy {egyetem.elotag()} iskola ami {egyetem.varos}-(ban/ben) található")
    



