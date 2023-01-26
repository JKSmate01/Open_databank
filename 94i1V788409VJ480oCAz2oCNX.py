from turtle import *
import random
def koch(h,sz):
    if sz == 0:
        forward(h)
    else:
        koch(h/3,sz-1)
        left(60)
        koch(h/3,sz-1)
        right(120)
        koch(h/3,sz-1)
        left(60)
        koch(h/3,sz-1)
reset()
up()
goto(-300,0)
down()
koch(600,5)
