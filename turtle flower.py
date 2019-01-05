from turtle import *
setup()
t1 = Turtle()
colors = ["red" , "blue"  , "yellow" , "orange" ,]
import random

t1.up()
t1.goto(-200,50)
t1.down()
t1.width(4)
t1.hideturtle()
for i in range(180):
    colorchoice = random.choice(colors)
    t1.color(colorchoice)
    t1.forward(400)
    t1.right(181)
    t1.speed(90)


    
