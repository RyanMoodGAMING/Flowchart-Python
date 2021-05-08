
# using easygui
# easygui gives a windows environtment for Python with simple commands
# here are some example programs using easygui - try them out!


from easygui import *
from random import *


def example_1():
    msgbox("Hello Everyone!")

def example_2():
    msgbox('Hello Everyone!','Buttons program')

def example_3():
    msgbox('Hello Everyone!','Buttons program','Click here!')

def example_4():
    ynbox("Do you like bananas? ", image="Bananas.gif")

def example_5():
    answer = ynbox("Do you like bananas? ", image="bananas.gif")
    if answer == True:
        msgbox("Me too! ")
    else:
        msgbox("Don't forget your five a day!!")    

def example_6():
    question = "What is the name of this fruit? "
    reply = buttonbox(question,image="bananas.gif",choices=["apple","banana","plum"])
    if reply == "banana":
        msgbox("Correct")
    else:
        msgbox("Incorrect")

def welcome():
    question01 = "What is the capital of England?"
    question02 = "What is the population of England?"
    question03 = "What is the population of Manchester in 2011."
    question04 = "What is the captial of France?"
    msgbox("""
Welcome to the Geography Quiz.
You are not allowed to use google.
""","Gegraphy Quiz")
    reply01 = buttonbox(question01,choices=["Manchester","Liverpool","London"])
    if reply01 == "London":
        msgbox("Correct!")
        reply02 = buttonbox(question02,choices=["5.32 million people","54.79 million people","10.47 million people"])
    else:
        msgbox("Incorrect.")
        reply02 = buttonbox(question02,choices=["5.32 million people","54.79 million people","10.47 million people"])
    if reply02 == "54.79 million people":
        msgbox("Correct! Well done.")
        reply03 = buttonbox(question03,choices=["497,777 people","65,650 people","2,000 people"])
    else:
        msgbox("Incorrect! Nice try.")
        reply03 = buttonbox(question03,choices=["92,028 people","65,650 people","2,000 people"])
    if reply03 == "497,777 people":
        msgbox("Correct, your very smart!")
        reply04 = buttonbox(question04,choices=["Paris","Manchester","Madrid"])
    else:
        msgbox("Incorrect, try again next time.")
        reply04 = buttonbox(question04,choices=["Paris","Manchester","Madrid"])
    if reply04 == "Paris":
        msgbox("Correct; well done.")
    else:
        msgbox("Incorrect; good luck next time.")


def password():
    password = passwordbox("Enter your password")
    while password != "admin":
        password = passwordbox("Incorrect, enter password")
    msgbox("Password correct")

def numbers():
    num_01 = enterbox("Enter a number")
    num_02 = enterbox("Enter another number")
    msgbox("Your 2 numbers were " + num_01 + " and "+ num_02)

def guessgame():
    msgbox("The computer is thining of a number...")
    computer_number = randint(1,101)
    msgbox("Can you guess the computer number?")
    guess = integerbox("Enter the number you guess was thought; 1 to 100") #The first guess.
    while guess != computer_number: 
        if guess > computer_number:
            msgbox("Too high.")
        elif guess < computer_number:
            msgbox("Too low.")
        guess = integerbox("Try again! 1 to 100")

def films():
    msgbox("You are going to have to chose your favourit Films from the following list.","Favourit Film")
    favfilm = choicebox("What is your faveourit Film?","Favourit Film",choices=["Sing","Mamma Mia","Mamma Mia 2","Avengers - End Game","","Other"])
    msgbox("Your favouit film is " + favfilm,"Favourit Film")
    
def password2():
    password = passwordbox("Enter your password")
    count = 0 
    while password != "admin":
        count = 0
        password = passwordbox("Incorrect, enter password")
    msgbox("Password correct")


    
    
    

        

