class Egyetem:
    def __init__(self,egyetemnév, város,nemzet):
        self.név = egyetemnév
        self.város = város
        self.nemzet = nemzet
    def nemzetiseg(self):
        if (self.nemzet == "a"):
            return "University."
        elif(self.nemzet == "n"):
            return "Universität"

