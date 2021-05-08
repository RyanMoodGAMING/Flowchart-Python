# My snowflake program.
# Ryan McAllister

import turtle
import random

wn = turtle.Screen()
wn.bgcolor("cyan")
rm = turtle.Turtle()
rainbow = ["black","white","black","brown","red","grey"]
rm.speed(1000)

for i in range(36):
    for j in range(2):
        rm.color(random.choice(rainbow))
        rm.forward(100)
        rm.right(60)
        rm.forward(100)
        rm.right(120)
    rm.right(10)

