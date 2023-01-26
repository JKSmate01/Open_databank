kacatok = ["csat","gombolyag","vonatjegy"]
print(kacatok)
kacatok.append("kulcskarika")
kacatok.append("egérfogó")
print(kacatok)
kacatok_felsorolva = ", ".join(kacatok)
print("A kacatjaim: ",kacatok_felsorolva, ".", sep="")
kacat="bármi"
while kacat != "elfogyott":
    kacat=input("Írj egy kacatot! ")
    if kacat != "elfogyott":
        kacatok.append(kacat)
kacatok_felsorolva = ", ".join(kacatok)
print("A kacatjaim: ",kacatok_felsorolva, ".", sep="")