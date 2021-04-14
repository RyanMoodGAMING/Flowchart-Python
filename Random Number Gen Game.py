# Random Number Guessing Game

from random import *

''''
Function: computerNumber
Parameters:
Return Value:
What it does: gets a random number 
''''

def guessNumber():
    numbers = []
    for i in range(4):
        number = 2
        numbers.append(str(number))
        
    print("(Debug) The random number is: " + numbers)

