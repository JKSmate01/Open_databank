import turtle
ablak = turtle.Screen()
Nori = turtle.Turtle()
for d in range(4):
    
    for i in range(4):
        Nori.forward(50)
        Nori.left(90)
    Nori.forward(50)


ablak.bgcolor("lightgreen")
ablak.title("Hello, 10e!")
Eszti = turtle.Turtle()
Eszti.color("blue")
ablak.mainloop()