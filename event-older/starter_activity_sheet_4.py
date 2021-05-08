# program written for Session 4
# Anything written after # is ignored by the computer
# We can use it to annotate programs to make them more readable

from turtle import *

# this line says we are using the "turtle" library of functions
# remember to use this for turtle graphics in Python


def square():
    fillcolor("Cyan")
    begin_fill()
    pencolor("Orange")
    forward (200) 
    right (90)
    forward (200) 
    right (90) 
    forward (200) 
    right (90) 
    forward (200)
    end_fill()

def triangle():
    fillcolor("Cyan")
    begin_fill()
    pencolor("Orange")
    penup()
    forward(120)
    right(120)
    forward(120)
    end_fill()

def Two():
    fillcolor("Orange")
    begin_fill()
    pencolor("Cyan")
    penup()
    forward(120)
    right(120)
    forward(120)
    pendown()
    penup()
    forward (210) 
    right (90)
    forward (200) 
    right (90) 
    forward (200) 
    right (90) 
    forward (200)
    end_fill()
    

#square()
triangle()
#Two()


