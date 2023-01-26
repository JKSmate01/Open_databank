ketrec = [2,5,4,6,7,2,3,4]
ossz_suly = 0
for i in range(len(ketrec)):
    ossz_suly += ketrec[i] 
print(f"Össz súlya: {ossz_suly}kg")
hkgfelett = 0
hkgfelett_tomeg = 0
otkgfelett = 0
for d in range(len(ketrec)):
    if (ketrec[d] >= 5):
        otkgfelett += 1
    elif (ketrec[d] >= 3):
        hkgfelett += 1
        hkgfelett_tomeg += ketrec[d]
print(f"3kg felett: {hkgfelett}db liba van. Ezeknek össz súlya {hkgfelett_tomeg}kg.")
print(f"5kg felett: {otkgfelett}db liba van.")
