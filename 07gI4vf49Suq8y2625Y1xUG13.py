from turtle import *
from random import randrange
def teglalap(x,y):

  begin_fill()

  forward(x)

  left(90)

  forward(y)

  left(90)

  forward(x)

  left(90)

  forward(y)

  end_fill()

def trikolor(f, k, a):

  fillcolor(f)

  teglalap(400,100)

  up()

  forward(100)

  left(90)

  down()

  fillcolor(k)

  teglalap(400,100)

  up()

  forward(100)

  left(90)

  down()

  fillcolor(a)

  teglalap(400,100)

  left(90)

def dikolor(felso, also):

  fillcolor(felso)

  teglalap(400,150)

  up()

  forward(150)

  left(90)

  down()

  fillcolor(also)

  teglalap(400,150)

  left(90)



reset()

color("gold")

szin = ["red","blue","yellow"]
x = randrange(3)
y = randrange(3)
while y == x:
    y = randrange(3)
z = randrange(3)
while z == y:
    z = randrange(3)
trikolor(szin[x],szin[y],szin[z])

up()

goto(-420,-50)

down()

dikolor("white","red")