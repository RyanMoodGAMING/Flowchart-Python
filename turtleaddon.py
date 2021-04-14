# Turtle Addon

from turtle import *

'''
Name of function: square()
Parameters: pen_color, fill_color, size
Return Value:
What it does:
'''
def square(pen_color, fill_color, size):
    pencolor(pen_color)
    fillcolor(fill_color)
    begin_fill()
    for i in range(4):
        pendown()
        forward(size)
        right(90)
    end_fill()

'''
Name of funcation: shape()
Parameters: pen_color, fill_color, sides, size
Return Value:
What it does:
'''
def shape(pen_color, fill_color, sides, size):
    pencolor(pen_color)
    fillcolor(fill_color)
    begin_fill()
    for i in range(sides):
        forward(size)
        right(360/sides)
    end_fill()

'''
Name of funcation: rectange()
Parameters: pen_color, fill_color, width, length
Return Value:
What it does:
'''
def rectange(pen_color, fill_color, width, length):
    pencolor(pen_color)
    fillcolor(fill_color)
    begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    end_fill()

'''
Name of funcation: triangle()
Parameters: pen_color, fill_color, length
Return Value:
What it does:
'''
def triangle(pen_color, fill_color, length):
    pencolor(pen_color)
    fillcolor(fill_color)
    begin_fill()
    for i in range(3):
        forward(length)
        right(45)
    end_fill()
        
    
