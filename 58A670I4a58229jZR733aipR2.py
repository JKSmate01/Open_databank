class KONYVTAR():
    def __init__(self,nev,varos,kotetek,nemzet):
        self.NEV = nev
        self.VAROS = varos
        self.KOTETEK = kotetek
        self.NEMZET = nemzet
    def kotetszam(self):
        if self.KOTETEK >= 50:
            return "ügyes gyűjtő"
        else:
            return "kevésbé szorgalmas"
    def nev_cim(self):
        return self.NEV.title()
    def nev_varos(self):
        return f"{self.NEV} az {self.VAROS}-ban helyezkedik el."
    def nev_hossz(self):
        return len(self.NEV)
    def nev_nemzetiseg(self):
        if str.lower(self.NEMZET) == "o":
            return f"{self.NEV} Biblioték"
        elif str.lower(self.NEMZET) == "b":
            return f"{self.NEV} Library"
