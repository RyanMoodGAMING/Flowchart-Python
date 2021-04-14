# Random Number Game


import random


'''
Name of Function: generateNumber
Parameters: None
Return Value: number, limit
What it does: Generates Random Number
'''
def generateNumber():
    limit = random.randint(100,1000) # choses the limit between 100 and 1000
    number = random.randint(1,limit)
    return number, limit

'''
Name of Function: playerGuest
Parameters: number, limit
Return Value: compare
What it does: inputs the guess and compares it to computer number.
'''
def playerGuess(number, limit):
    guess = int(input("Guess my number between 1 and %s . " %limit)) # inputs the player's guess
    if  guess == number: # if statement to see if the number is the same as the input
        compare = "correct" 
    elif guess < number: # elif - else if statement to see if its smaller than
        compare = "too low" 
    else:                # else - else statement to say if something is diffrent to other 2 if's.
        compare = "too high"
    return compare # returns 'compare' value


randnumber, randlimit = generateNumber() # gets the random generated number
#print(randnumber) # Used for testing
player_input = "incorrect"
while player_input != "correct": # keeps the code going untill the word "correct" is said
    player_input = playerGuess(randnumber, randlimit) # gets the player input and replaces player_input
    print(player_input) # says what playerGuess says
print("Well done!") # Tells the player "Well done"
