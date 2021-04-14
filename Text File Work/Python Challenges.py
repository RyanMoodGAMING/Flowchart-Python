# Python Challenges

import random
import time


'''
Name of Function: challenge1
Parameters: None
Return Value: age
What it does: Gets the user's age and says the User's name.
'''
def challenge1():
    validity = False
    while validity != True:
        age = input("Please input your age (below 150): ")
        for i in range(len(age)):
            if age[i] not in "0123456789" or int(age) > 150 or age == str():
                validity = False
                print("""
That is not a valid answer
""")
                age = input("Please input your age: ")
            elif age[i] in "0123456789":
                validity = True

    age = int(age)
    print("Your age is " + str(age))


'''
Name of Function: challenge2
Parameters: None
Return Value: average
What it does: The user will input 2 numbers then  tells us the average of the 2 numbers.
'''
def challenge2():
    number1 = int(input("Input number 1 -> "))
    number2 = int(input("Input number 2 -> "))
    average = number1 + number2 / 2
    print("The average  of " + str(number1) + " and " + str(number2) + "and the average is " + str(average))


'''
Name of Function: challenge3
Parameters: None
Return Value: area
What it does: The user has to input the length and width and then works out the area.
'''
def challenge3():
    length = int(input("Please enter your length -> "))
    width = int(input("Please enter your width -> "))
    area = length * width
    print("Your area is " + str(area))

'''
Name of Function: challenge4
Parameters: None
Return Value: div (answer)
What it does: Gets the user to imput two numbers and then divides them.
'''
def challenge4():
    number1 = int(input("Please enter number 1 -> "))
    number2 = int(input("Please enter number 1 -> "))
    div = number1 / number2
    print("The answer to " + str(number1) + " devided by " + str(number2) + " is " + str(div))

'''
Name of Function: challenge5
Parameters: None
Return Value: favesubject, name
What it does: Asks the user what they name and faveourite subject is and then tells the user a message.
'''
def challenge5():
    name = input("What is your name? -> ")
    favesubject = input("What is your favouite subject, " + name + " -> ")
    print("My favourite subject is also " + favesubject + ", "+ name + "!")


'''
Name of Function: challenge28
Parameters: None
Return Value: i, randomname
What it does: Gets the user to input 5 names and then works out a random one.
'''
def challenge28():
    names = []
    complete = False
    while complete != True:
        try: 
            for i in range(5):
                name = input("Please enter " + str(i + 1) + " name -> ")
                names.append(name)
            #print(names[0] + names[1] + names[2] + names[3] + names[4]) # Debug Tool
            randomname = random.choice(names)
            print()
            print("You entered " + str(i + 1) + """ names.
The name selected is """ + randomname)
            complete = True
            
        except:
            print("""
An error occured! Sorry for any inconvinince.
""")
            names = []

'''
Name of Function: clear
Parameters: None
Return Value: None
What it does: Clears the shell.
'''
def clear():
    for i in range(200):  
        print("""


    """)

'''
Name of Function: challenge10
Parameters: None
Return Value: Win, Don't Win
What it does: It makes a choice (rock, paper or scissors) and then the user has to try and input it and says who has won.
'''
def challenge10():
    choices = ["rock", "paper", "scissors"]
    computerchoice = random.choice(choices)
   # print("(Debug) COMPUTER CHOICE --> " + computerchoice) #Un-comment me to use the debug tool (the beginging not this one).
    playerchoice = input("Please input your choice (rock, paper or scissors). ")
    while playerchoice.lower() not in choices:
        print("You didn't input a valid choice.")
        playerchoice = input("Please input your choice (rock, paper or scissors). ")
        print()
   # print("Valid")
    if computerchoice == playerchoice.lower():
       print("You and the computer had a draw.")
##    else:
##        print("You can the computer got diffent answers!")
##        print()
##        print("You put " + playerchoice.lower() + " and the computer put " + computerchoice + ".")
    elif playerchoice.lower() == "rock":
        if computerchoice  == "paper":
            print("Computer Wins. It selected " + computerchoice)
            print("You chosen " + playerchoice.lower())
        elif computerchoice == "scissors":
            print("You won! You chosen " + playerchoice.lower())
            print("The computer put " + computerchoice)
        #print("(Debug) We got to player choice = rock") #Un-comment me to use the debug tool (the beginging not this one).
    elif playerchoice.lower() == "scissors":
        if computerchoice  == "rock":
            print("Computer Wins. It selected " + computerchoice)
            print("You chosen " + playerchoice.lower())
        elif computerchoice == "paper":
            print("You won! You chosen " + playerchoice.lower())
            print("The computer put " + computerchoice)
       # print("(Debug) We got to player choice = scissors") #Un-comment me to use the debug tool (the beginging not this one).
    elif playerchoice.lower() == "paper":
        if computerchoice  == "rock":
            print("Computer Wins. It selected " + computerchoice)
            print("You chosen " + playerchoice.lower())
        elif computerchoice == "scissors":
            print("You won! You chosen " + playerchoice.lower())
            print("The computer put " + computerchoice)
      #  print("(Debug) We got to player choice = paper") #Un-comment me to use the debug tool (the beginging not this one).

'''
Name of Function: challenge11
Parameters: None
Return Value: 
What it does: User inputs a sentence then works out and outputs how many charaters there is in a sentance.
'''
def challenge11():
    sentence = input("Please enter a sentence that you would like us to check how many charters there is in there.")
    charaters = len(sentence)
    print("There is " + str(charaters) + " in the sentence")

'''
Name of Function: challenge25()
Parameters: None
Return Value: 
What it does:
'''
def challenge25():
    applyChoices = ["yes", "no"]
    print("Would you like to apply for an after school club? ")
    apply = input("Yes or No -> ")
    while apply.lower() not in applyChoices:
        print("You entered an invalid choice. ")
        print("Would you like to apply for an after school club? ")
        apply = input("Yes or No -> ")
    if apply.lower() != "no": 
        firstName = input("Please input your first name. ")
        sureName = input("Please input your sure name. ")
        genderChoice = ["male", "female", "other", "don't wish to say"]
        gender = input("Please input your gender. ")
        while gender.lower() not in genderChoice:
            print("You have inputted an invalid choice! ")
            gender = input("Please input your gender ")
        form = input("Please enter your Form Group! ")
        textFile = open("challenge25-applyafterschoolclub.txt", "a")
        textFile.write("\n")
        textFile.write("Name --> " + firstName + " " + sureName)
        textFile.write("\n")
        textFile.write("Gender --> " + gender)
        textFile.write("\n")
        textFile.write("Form Group --> " + form)
        textFile.write("\n \n")
        textFile.close()
    else:
        print("We are here for later!")

'''
Name of Function: challenge26()
Parameters: None
Return Value:
What it does:
'''
def challenge26():
    textFile = open("MathsQuiz.txt", "a")
    points = 0
    name = input("Please input your name!")
    question1 = input("What is 2 + 9? ")
    answer1 = 2 + 9
    question2 = input("What is 2 x 2? ")
    answer2 = 2 * 2
    question3 = input("What is 25 / 5? ")
    answer3 = 25 / 5
    if answer1 == question1:
        points = points + 1
    elif answer1 != question1:
        points = points
    elif answer2 == question2:
        points = points + 1
        
    print("Were going to ask you some questions!")
    textFile.write("\n")
    textFile.write("-=-=-=-=-=-=-=-=-=-=-")
    textFile.write("Name -->       " + name + "\n")
    textFile.write("Question 1 --> ")
    textFile.write("Question 2 --> ")
    textFile.write("Question 3 --> ")
    textFile.close()

'''
Name of Function: challenge6()
Parameters:
Return Value:
What it does:
'''
def challenge6():
    name = input("What is your name? -> ")
    if name == "Ryan":
        print("You're cool.")
    else:
        print("Nice to meet you, " + name)

'''
Name of Function: challenge12()
Parameters:
Return Value:
What it does: Gets the user to input a sentence then outputs it in uppper case.
'''
def challenge12():
    sentence = input("Please input a sententence you want to be in uppercase -> ")
    print(sentence.upper())


'''
Name of Function: challenge13()
Parameters:
Return Value:
What it does: Asks the user ot input a sentence then asks the user to input the word they want to repleace and the word they want to replace it with then outpiuts the new sentence.
'''
def challenge13():
    sentence = input("Please input the sentence you want to input. -> ")
    changeWord = input("What word would you like to change? -> ")
    replacementWord = input("What word would you like to replace it with? -> ")
    sentence = sentence.replace(changeWord, replacementWord)
    print("The new sentence is -> " + sentence)
        

'''
Name of Function: challenge28()
Parameters:
Return Value:
What it does: Asks the user was to input a sentence and then outputs the number of times the word 'the' occurs in it.
'''
#def challenge14():
    
'''
Name of Function: challenge20()
Parameters:
Return Value:
What it does: Asks he program to input put a number then reap it it until they guess the number 7 and then says a message.
'''
def challenge20():
    number = int(input("Pleae input a number. -> "))
    while number != 7:
        number = int(input("Pleae input a diffrent number. -> "))
    print("Well Done! ")

'''
Name of Function: challenge26()
Parameters:
Return Value:
What it does: A math quiz, and works out the score.
'''
def challenge26():
    name = input("What is your name? -> ")
    score = 0
    questionOne = input("What is 2 * 2? -> ")
    questionTwo = input("What is 5 + 3? -> ")
    questionThree = input("What is 5 - 2? -> ")
    answerOne = 2*2
    answerTwo = 5+3
    answerThree = 5-2
    if questionOne == answerOne:
        score = score + 1
    if questionTwo == answerTwo:
        score = score + 1
    if questionThree == answerThree:
        score = score + 1
    print(name + " you got a score of " + str(score) + "/3. ")

    txtFile = open("challenge26.txt", 'a')
    txtFile.write("---------------------- Math Quiz ---------------------- \n")
    txtFile.write("Q1 -> " + questionOne + " (correct answer is -> " + answerOne + ")")
    txtFile.write("Q2 -> " + questionTwo + " (correct answer is -> " + answerTwo + ")")
    txtFile.write("Q3 -> " + questionThree + " (correct answer is -> "+ answerThree + ")")
    txtFile.write(
    
    


end = False
while end == False:
    try:
        time.sleep(10)
        clear()
        print("To clear the shell type clear()")
        choices = ["1", "2", "3", "4", "5", "6", "10", "11", "28", "25","12", "13", "20", "clear", "end"]
        userchallengechoice = input("Please enter the number of the challenge you would like to look at (1, 2, 3, 4, 5, 10, 11, 12, 13, 20 25, 28, end) --> ")
        while userchallengechoice not in choices:
            print()
            print("You didn't input a valid choice.")
            userchallengechoice = input("Choice one: 1, 2, 3, 4, 5, 10, 11, 12, 13, 20, 25, 28, end --> ")
        if userchallengechoice == "1":
            clear()
            challenge1()
        elif userchallengechoice == "2":
            clear()
            challenge2()
        elif userchallengechoice == "3":
            clear()
            challenge3()
        elif userchallengechoice == "4":
            clear()
            challenge4()
        elif userchallengechoice == "5":
            clear()
            challenge5()
        elif userchallengechoice == "6":
            clear()
            challenge6()
        elif userchallengechoice == "10":
            clear()
            challenge10()
        elif userchallengechoice == "11":
            clear()
            challenge11()
        elif userchallengechoice == "12":
            clear()
            challenge12()
        elif userchallengechoice == "13":
            clear()
            challenge13()
        elif userchallengechoice == "20":
            clear()
            challenge20()
        elif userchallengechoice == "25":
            clear()
            challenge25()
        elif userchallengechoice == "28":
            clear()
            challenge28()
        elif userchallengechoice == "clear":
            clear()
        elif userchallengechoice == "end":
            clear()
            end = True
    except:
        print("An error occurded! Restarting...")
