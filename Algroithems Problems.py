# Algerithem Problems

'''
Name of Function: areaRectangle
Parameters: 
Return Value: Area
What it does: Works out the area of the Rectangle
'''

def areaRectangle():
    length = int(input("Please enter the length of the rectangle. "))
    width = int(input("Please enter the width of the rectangle. "))
    area = length*width
    #print("Your area is ",  area)
    return area

'''
Name of Function: radiusCircle
Parameters: 
Return Value: Radius
What it does: Works out the radius of a Circle
'''
def radiusCircle():
    radius = int(input("Please enter the radius of the Circle. "))
    area = 3.14*radius*radius
    print("The result is ", area)

'''
Name of Function: randnumber
Parameters: 
Return Value: total
What it does: Works out the total of the 2 numbers entered.
'''
def randnumber():
    number1 = int(input("Plese enter a number inbetween 1-9! "))
    number2 = int(input("Please enter another number inbetween 1-9! "))
    while number1 < 0 or number1 >9:
        number1 = int(input("Plese enter a number inbetween 1-9! "))
    while number2 < 0 or number2 >9:
        number2 = int(input("Plese enter a number inbetween 1-9! "))
    total = number1*number2
    print("The total of the 2 numbers is (multifiled) ", total)


'''
Name of Function: advice
Parameters: 
Return Value: message
What it does: Displays something if Y is pressed.
'''
def advice():
    request = input("Click a button (Y is recommended). ")
    if request.upper()[0] == 'Y':
        print("DJ RJ is your best local DJ.")

'''
Name of Function: darts
Parameters: 
Return Value: A message
What it does: lets you input your darts score.
'''

def darts():
    score = int(input("Please enter your darts score! 0 - 180. "))
    while score > 180:
        print("You entered a number too high.")
        score = int(input("Please enter your darts score! 0 - 180. "))
    if score > 100:
        print("Very good! ")
    elif score < 10:
        print("Some practise is required!")
    else:
        print("Try again next time. Above 10 is also good!")

'''
Name of Function: charity
Parameters: 
Return Value: dubbled
What it does: Gets the 3 diffrent friends amounts then adds them then if it is 1000 or is above 1000 it dubbles it.
'''

def  charity():
    friend1 = int(input("Friend 1 please enter the amount you recived / made! "))
    friend2 = int(input("Friend 2 please enter the amount you recived / made! "))
    friend3 = int(input("Friend 3 please enter the amount you recived / made! "))
    friendstotal = friend1+friend2+friend3

    if friendstotal >= 1000:
        print("Dubbling...")
        dubbled = friendstotal*2
    else:
        dubbled = friendstotal
    print("You made ", dubbled)

'''
Name of Function: twoRectangles
Parameters: 
Return Value: area, area2
What it does: Gets 1st rectangle length and width and then the 2nd rectangle length and width.
'''
def twoRectangles():
    area1 = areaRectangle()
    area2 = areaRectangle()
    #print("Your area is ",  area)
    print("Your first rectangle is ", area1, " and the area for the second area is ", area2)
    if area1 < area2:
        print("Area 2 is bigger -> ", area2)
    elif area2 < area1:
        print("Area 1 is bigger -> ", area1)
    else:
        print("Area 1 and Area 2 is the same.")


'''
Name of Function: punishment
Parameters: 
Return Value: lines
What it does: Gets the user to input a line then repeats it 20 times.
'''

def punishment():
    line = input("Please input your line. ")
    counter = 0
    for counter in range(20):
        print(line)
'''
Name of Function: golfScore
Parameters: 
Return Value: total
What it does: It gets the user to input 6 scores then works out the total
'''
def golfScore():
    score1 = input("Please enter your 1st score.")
    score2 = input("Please enter your 2nd score.")
    score3 = input("Please enter your 3rd score.")
    
    score4 = input("Please enter your 4th score.")
    score5 = input("Please enter your 5th score.")
    score6 = input("Please enter your 6th score.")

    total = score1+score2+score3+score4+score5+score6
    print("Your total score is ", total)

'''
Name of Function:  dartScoreComp
Parameters: 
Return Value: total
What it does: It gets both players to enter there scores then says the winner.
'''

def dartScoreComp():
    player1 = []
    player2 = []
    for i in range(9):
        score1 = int(input("Player 1 please enter your score. "))
        score2 = int(input("Player 2 please enter your score. "))
        player1.append(score1)
        player2.append(score2)
      #  print(player1, player2)
    total1 = player1[0]+player1[1]+player1[2]+player1[3]+player1[4]+player1[5]+player1[6]+player1[7]+player1[8]
    total2 = player2[0]+player2[1]+player2[2]+player2[3]+player2[4]+player2[5]+player2[6]+player2[7]+player2[8]
    if total1 < total2:
        print("Player 2 is the winner ", total2)
    elif total2 < total1:
        print("Player 1 is the winner ", total1)
    else:
        print("The winner is Player 1 and Player 2. Player 1 Score is %s and the total of Player 2 is "%total1, total2)
