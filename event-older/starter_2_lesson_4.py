#starter program for drawing the envelope in lesson 4
# Anything written after # is ignored by the computer
# We can use it to annotate programs to make them more readable

from turtle import *
from math import *

# this line says we are using the "turtle" library of functions
# remember to use this for turtle graphics in Python

def square(side):
    for counter in range(4):
        forward (side)
        right(90)

def triangle(side):
    forward(side)
    right(120)
    forward(side)
    right(120)
    forward(side)
    right(120)
        
    
