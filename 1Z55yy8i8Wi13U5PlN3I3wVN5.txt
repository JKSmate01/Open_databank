out = open("H:\out.txt","w")
reggeli = {'tea', 'vaj', 'piritós','sajt'}
ebed = set() #üres
ebed = set(["halászlé","kenyér",True])
print(reggeli)
print(ebed)
out.write(f"{reggeli}\n")
out.write(f"{ebed}\n")
# egy elem hozzáadása
reggeli.add('lekvár')
print(reggeli)
out.write(f"{reggeli}\n")
    # egy nem meghatározott elem eltávolítása
reggeli.pop()
print(reggeli)
out.write(f"{reggeli}\n")
    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, akkor hibát eredményez
reggeli.remove('sajt')
print(reggeli)
out.write(f"{reggeli}\n")
    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, nem eredményez hibát
reggeli.discard('sajt')
print(reggeli)
out.write(f"{reggeli}\n")

#Szótár
raktar = {}
print(raktar)
out.write(f"{raktar}\n")
diak = {
    "vezeteknev":"Kiss",
    "keresztnev": "Péter",
    "eletkor" : 17,
    "menza" : True
}
print(diak["eletkor"])
print(diak.get("eletkor"))
print(diak.get("kollegista","nem"))
print("keresztnev" in diak)
out.close()
