from konyvtar_alap import KONYVTAR


konyvtarak = []
for i in range(3):
    nev = input("Adja meg a könyvtár nevét: ")
    varos = input("Adja meg a könyvtár városát: ")
    kotetek = int(input("Adja meg a kötetek mennyiségét(millió): "))
    konyvtarak.append(KONYVTAR(nev,varos,kotetek))

for konyvt in konyvtarak:
    print(f"{konyvt.kotetszam()} címet kapott {konyvt.nev_cim()} {konyvt.nev_nemzetiseg()} {konyvt.KOTETEK} millió gyüjtött kötettel, {konyvt.nev_varos()}, neve {konyvt.nev_hossz()} hosszúságú")
