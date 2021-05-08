# starter program week 2 - perhaps this could be a task

def conversation(): #Used to make an define.
    print("Welcome to my conversation program")#It prints whats in the colons and in the "".
    print()
    answer = input("Do you like Sports?")
    if answer == "yes":
        print("Doing sports is good for your fitness.")
    else:
        print("You might like sports in the feature.")
    print()#It leaves a gap.
    print("Do you like cycling? Answer yes or no")#Asks the question if the person likes cycling.
    answer1 = input()#Gets the varible "answer" and then says input() for the user to put answer.
    if answer1 == "yes":#detects if the user put yes.
        print("That's good - you will get very fit")
    else: #Detects if the user puts the anyother words than "yes".
        print("Perhaps you like some other sport. ")
    print("Goodbye") #Says the goodbye messages.

#conversation() #makes the program work.

def cities():
    print("This quiz will ask you about Cities!")
    print()
    answer2 = input("How many cities are the in England?")
    if answer2 == "51":
        print("Correct.")
    else:
        print("Incorrect.")
    print("Goodbye!")

#cities()

def numbers():
    print("Please enter a number bigger than 10!")
    number = int(input())
    print("You number was ", number, ".")
    print("I wonder if you entered it correctly.")
    if number > 10:
        print("Entered correctly.")
    else:
        print("Entered incorrectly.")

#numbers()

def score():
    print("Please tell me your score.")
    number2 = int(input())
    print("You entered ", number2, ".")
    if number2 > 50:
        print("You have passed the test.")
    else:
        print("You failed the test.")

#score()

def age():
    print("Please tell me your age!")
    number3 = int(input())
    if number3 >13:
        print("Time to earn some cash! You can do paper rounds.")
    else:
        print("Your not old enough to ear some cash, you can't do the paper round.")

age()




    
