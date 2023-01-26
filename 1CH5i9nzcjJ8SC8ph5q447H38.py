


def e1():
    név = input("Mi az ős neve? ")
    bogyók = int(input("Hány bogyója van? "))

    if (bogyók < 10):
        minősítés = "zsenge"
    elif(bogyók > 20):
        minősítés = "nagy koponya"
    else:
        minősítés = "gyüjtögető"

    print(f"{név} egy {minősítés}.")

def e2():
    B_Q = int(input("Mennyi barack termett (mázsa)? "))
    b_ar = int(input("Milyen áron? "))
    K_Q = int(input("Mennyi körte termett (mázsa)? "))
    k_ar = int(input("Milyen áron? "))
    print(f"{B_Q} mázsa barack termet amit {b_ar}FT/kg áron lehet venni. Termett még körte is {K_Q} mázsa, {k_ar}FT/kg áron.")
    print(f"Ha az összes barackot elakarja adni {B_Q *100*b_ar}FT-ot keresne, ha a körtét eladná abból {K_Q * 100*k_ar}FT.")
    if (B_Q * 100*b_ar > K_Q * 100*k_ar):
        print("Barack eladással jobban jár!")
    elif (B_Q * 100*b_ar < K_Q * 100*k_ar):
        print("Körte eladással jobban jár!")
    print("De legjobban akkor jár ha mindkettőt eladja!")
e2()