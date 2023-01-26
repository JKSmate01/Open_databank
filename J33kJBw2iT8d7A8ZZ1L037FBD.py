import hires_film_alap as hfa
filmek = []
for _ in range(3):
    neve = input("Add meg egy híres film címét! ")
    h = int(input("Add meg a hosszát! "))
    nemzet = input("Add meg a nemzetiségét (GB/USA)! ")
    filmek.append(hfa.HíresFim(neve,h,nemzet))
for film in filmek:
    print(f"{film.cím} egy híres {film.hossz} perces {film.orszag()} film.")
