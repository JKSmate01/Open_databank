import hiresegyetem_alap as ha
egyetemek = []
for _ in range(3):
    nev = input("Add meg egy egyetem nevét! ")
    varos = input("Add meg a az egyetem városát! ")
    nemzet = input("Add meg a nemzetiségét (a/n)! ")
    egyetemek.append(ha.Egyetem(nev,varos,nemzet))
for egyetem in egyetemek:
    print(f"{egyetem.nemzetiseg()} {egyetem.név} egy híres {egyetem.város} egyetem")
