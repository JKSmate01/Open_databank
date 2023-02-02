class HíresFim:
    def __init__(self,cime,hossz,nemzet):
        self.cím = cime
        self.hossz = hossz
        self.nemzet = nemzet
    def orszag(self):
        if (self.nemzet == "USA"):
            return "amerikai"
        elif (self.nemzet == "GB"):
            return "angol"



