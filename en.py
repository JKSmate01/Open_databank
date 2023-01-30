import os
import random as r
import string
from datetime import datetime
print(r.choice(string.ascii_letters))
folder = r'.\\'
out = open("H:\\Feladatok\\2022-2023\\Python\\feladatok\\list.txt", "a")
def ra():
    for fn in os.listdir(folder):
        if (fn != "en.py" and fn != "list.txt"):
            s = folder + fn
            ty = ""
            for i in range(len(fn)):
                if(fn[i] == "."):
                    ty = fn[i+1:]
                    break
            deso = ""
            for d in range(25):
                rd = r.randint(0,1)
                if(rd == 0):
                    deso += r.choice(string.ascii_letters)
                else:
                    deso += str(r.randint(0,9))
            des = folder + deso + "." + ty
            os.rename(s,des)
            now = datetime.now()
            today = datetime.today()
            out.write(f"{fn} = {des}  || {today} \n")
w = input("Fájl neve (a -> összes | d -> decode): ")
if (w == "a"):
    ra()
elif(w == "d"):
    out.close()
    re = open("H:\\Feladatok\\2022-2023\\Python\\feladatok\\list.txt", "r")
    fn = input("Adja meg a fájl nevét! ")
    for i in re:
        if fn in i:
            print(i)
            s = i.index(".\\")+3
            while i[s] != " ":
                s+=1
            idd = i.index(".\\")+3
            print(f"https://github.com/JKSmate01/Open_databank/blob/main/{i[idd:s]}")
            break
    re.close()
else:
    s = folder + w
    for i in range(len(w)):
        if(w[i] == "."):
            ty = w[i+1:]
            break
    deso = ""
    for d in range(25):
        rd = r.randint(0,1)
        if(rd == 0):
            deso += r.choice(string.ascii_letters)
        else:
            deso += str(r.randint(0,9))
    des = folder + deso + "." + ty
    os.rename(s,des)
    now = datetime.now()
    today = datetime.today()
    print(f"{w} = {des}  || {today}")
    out.write(f"{w} = {des}  || {today} \n")
out.close()
