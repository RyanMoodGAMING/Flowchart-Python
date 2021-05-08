# starter program week 7

import random

# pizza

def pizza(): #Defination of the code
             #The program says "What toppings would you like on your pizza? All pizzas have cheese. "
    print("What toppings would you like on your pizza? All pizzas have cheese. ")
    print("Enter X when you have finished adding toppings. ") #Says "Enter X when you have finished adding toppings."
    toppings = "" # This is a viruball.
    next_topping = "" # This is a viruball.
    while next_topping != "X": #Keeps reaping the code below.
        print("So far you have a pizza with cheese " + toppings)
        next_topping =  input("Enter topping ... ")
        if next_topping != "X":
            toppings = toppings + " and " + next_topping
            print("Add your next topping (X when finished)")
    print("Your pizza will have cheese " + toppings + ". Enjoy! ")


def shopping_list():
    print("Play this with your partner")
    bought = input("What did you buy? ")
    next_bought = ""
    while next_bought != "X":
        print("I went shopping and I bought " + bought)
        next_bought =  input("What did you buy? ")
        if next_bought != "X":
            bought = bought + " and " + next_bought
            
            print("What did you buy? (X when finished)")
    print("I went shopping and bought " + bought + ".")
    print("End of game!")

def guessing():
    print("The computer is thinking of a number... ")
    computer_number = random.randint(1,100) #Thinks of the number
    print("Can you guess the computer's number")
    guess = int(input("Enter you guess here: ")) #The first guess.
    while guess != computer_number: 
        if guess > computer_number:
            print("Too high.")
        elif guess < computer_number:
            print("Too low.")
        guess = int(input("Enter you guess here: "))
    print("You guessed the correct number.")

def extension():
    print("I will now print the letters A to Z")
    althabet = ""
    while althabet != "90":
        print(chr(65))
    

#pizza()
#shopping_list()    
guessing()
#extension()
