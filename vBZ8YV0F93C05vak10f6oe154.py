wr = open("H:\\out.txt","w")
wr.write("res\n")
wr.write("redss\n")
wr.write("raaes\n")
wr.close()
re = open("H:\\out.txt","r")
line = re.readline()
while line != "":
    line = line.strip()
    print(line)
    line = re.readline()
re.close()
print("next")
re = open("H:\\next.txt","r")
line = re.readline()
while line != "":
    line = line.strip()
    print(line)
    line = re.readline()
re.close()
#Ki írni
re = open("H:\\adat.txt","r")
line = re.readline()
while line != "":
    line = line.strip()
    datas = line.split()
    print(datas[0],datas[1],datas[2],datas[3],datas[4])
    print(line)
    line = re.readline()
re.close
#Elvégezni a műveletet
re = open("H:\\adat.txt","r")
line = re.readline()
ossz = 0
while line != "":
    line = line.strip()
    datas = line.split()
    if (datas[4] == "+"):
        ossz = 0
        for i in range(0,4):
            ossz += int(datas[i])
        print(datas[0],datas[1],datas[2],datas[3],datas[4], "= ",ossz)
    if (datas[4] == "*"):
        ossz = 1
        for i in range(0,4):
            ossz *= int(datas[i])
        print(datas[0],datas[1],datas[2],datas[3],datas[4], "= ",ossz)
    #print(line)
    line = re.readline()
re.close()
