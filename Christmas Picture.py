# Christmas Picture 

from turtle import *
from random import *
from turtleaddon import *

##complete = False
##while complete != True:
##    try: 
bgcolor("Black")

'''
Name of Function -> snow()
Parameters ->
Return Value ->
What it does -> It makes a big white square that acts like snow.
'''
def snow():
    fillcolor("white")
    begin_fill()
    speed(200)
    for i in range(4):
        forward(2000)
        right(90)
        forward(2000)
    end_fill()

'''
Name of Function -> snowflakes()
Parameters ->
Return Value ->
What it does -> 
'''

def snowflakes(): 
    number = randint(5, 8)
    speed(2000)
    pencolor("white")
    for i in range(number):
        for i in range(number):
            pendown()
            forward(5)
            left(45)
            forward(5)
            back(5)
            right(90)
            forward(5)
            back(5)
            left(45)
        back(number * 5)
        right(360/number)
        penup()
        
        
'''
Name of function -> santa()
Parameters ->
Return Value ->
What it does ->
'''

def santa():
    goto(0,0)
    pencolor("red")
    fillcolor("red")
    begin_fill()
    penup()
    pendown()
    circle(60)
    end_fill()
    goto(0,60)
    penup()
    right(360)
    pendown()
    rectange("black","black",5,60)
    penup()
    left(90)
    left(90)
    forward(5)
    right(90)
    pendown()
    rectange("black","black",5,60)
    penup()
    left(90)
    left(90)
    forward(45)
    right(90)
    forward(15)
    pendown()
    pencolor("yellow")
    fillcolor("yellow")
    begin_fill()
    circle(30)
    end_fill()
    


snow()
santa()
penup()
for i in range(4):
    number = randint(50,200)
    goto(200,0)
    forward(number)
    left(90)
    forward(number)
    right(15)
    forward(number)
##    goto(-number,number)
    pendown()
    snowflakes()
complete = True
##    except:
##        print("An error occoured! Restarting the program.")

'''
Name of Funcation: chatclear()
'''
def chatclear():
    for i in range(200):
        print(" ")
