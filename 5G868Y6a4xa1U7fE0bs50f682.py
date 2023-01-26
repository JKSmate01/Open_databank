
from time import sleep


wr = open("H:\egyeb\osz.txt","w") #w = létrehoz ha nincs
wr.write("Őszi szünet\n") #\n új sor
wr.write("2022. november 7. napon Tanítás az iskolában.\n")
wr.close()

szamok  = open("H:\egyeb\szamok.txt","w")
for i in range(1,101):
    szamok.write(f"{i}\n")
szamok.close()
