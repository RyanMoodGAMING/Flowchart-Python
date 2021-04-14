# Game

import random

# Imports random modual

'''
Name of Function: generateNumber
Parameters: None
Return Value: code
What it does: Generates Random Number
'''
def generateNumber():
    code = ""
    for i in range(4):
        number = random.randint(0,9)
        while str(number) in code:
            number = random.randint(0,9)
            print("Changed NUMBER")
        code += str(number)
    return code
    
'''
Name of Function: bullCount
Parameters: code, guess
Return Value: bulls
What it does: Works out how many bulls you get.
'''

def bullCount(code, guess):
    bulls = 0
    for i in range(4):
         if code[i] == guess[i]:
             bulls = bulls + 1
    return bulls

'''
Name of Function: cowCount
Parameters: code, guess, bulls
Return Value: cows
What it does: Works out how many cows you get.
'''

def cowCount(code, guess, bulls):
    cows = 0
    for i in range(4):
        if code[i] in guess:
            cows = cows + 1
    cows = cows - bulls
    return cows

'''
Name of function: checkGuess
Parameters: guess
Return Value: True/False
What the function does:
Checks if the player's guess is valid

'''
def checkGuess(guess):
   
    if guess == "exit":
        return True
    if len(guess) != 4:
        return False
    for i in range(4):
        if guess[i] not in "0123456789":
            return False
        if guess.count(guess[i]) > 1:
            return False
    return True
        
'''
Name of function: mainGame
Parameters:
Return Value: True/False
What the function does: The actual game

'''
def mainGame():
    try:
        win = False
        code = generateNumber()
        guess_amount = 0
        # Un-comment this if you you need to test the Winning Function 
        print("Debug Tool: code is " + code)
        while win != True:
            guess = input("""If you wish to exit type EXIT or click CTRL + C,
Please enter a 4 digit number: """)
            
            while checkGuess(guess) != True:
                print("There was an error! Try again!")
                guess = input("Please enter a 4 digit number: ")
            guess_amount = guess_amount + 1
            bulls = bullCount(code, guess)
            cows = cowCount(code, guess, bulls)
            print(str(bulls) + " Bulls, " + str(cows) + " Cows.")
            if guess != code:
                win = False
            elif guess == exit:
                win = True
                print("Well done! You got the right answer.")
                print("You got " + bulls + "  bulls and " + cows + " cows.")
                print("You guessed " + guess + "and the code was " + code)
                print("You guessed " + guess_amount + " times. ")
                #return True
            else:
                win = True
                print("Well done! You got the right answer.")
                print("You got " + bulls + "  bulls and " + cows + " cows.")
                print("You guessed " + guess + "and the code was " + code)
                print("You guessed " + guess_amount + " times. ")
                #return True
    except KeyboardInterrupt:
        print("Ok, we will exit the game for you! The generated number was " + str(code))
        return True 


##try:
##    play_game = True
##    while play_game == True:
##        again = input("Would you like to play the game? ")
##        if again.lower()[0] == "y":
##            mainGame()
##        else:
##            play_game = False
##except:
##    print()
##    print("An error occured. We will be exiting the program.")
##    print("If you want to play the game please restart the program.")
