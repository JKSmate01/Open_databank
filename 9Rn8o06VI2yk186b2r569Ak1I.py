class Balaton:
    def __init__(self, település,lakok, fekvés):
        self.település = település
        self.fekvés = fekvés
        self.lakok = lakok
    def fekvese(self):
        if(self.fekvés == "é"):
            return "északi"
        elif(self.fekvés == "d"):
            return "déli"
    def lakossag(self):
        if (self.lakok < 5000):
            return "falu"
        elif(self.lakok > 5000 and self.lakok < 10000):
            return "nagyközség"
        elif(self.lakok >= 10000):
            return "város"
telepulesek = []
for _ in range(3):
    neve = input("Add meg egy település nevét! ")
    fekves = input("Add meg a fekvése (é/d)! ")
    menny = int(input("Add meg a lakosság számát! "))
    telepules = Balaton(neve,menny,fekves)
    telepulesek.append(telepules)
for tel in telepulesek:
    print(f"{tel.település} egy {tel.fekvese()} parti {tel.lakossag()}, {tel.lakok} fővel.")



