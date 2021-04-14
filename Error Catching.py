# Error Chaching

'''
Name of Function: error1
Parameters: 
Return Value: 
What it does: Error Chatching #1, if the user is below 18.
'''
def error1():
    age = int(input())
    if age<18:
        print(child)


'''
Name of Function: error2
Parameters: 
Return Value: 
What it does: Error Chatching #2, post letters
'''
def error2():
    for x in range(10):
        print("abcdefjklm"[x])


'''
Name of Function: error3
Parameters: 
Return Value: 
What it does: Error Chatching #3, work otu a length/width
'''
def error3():
    length = int(input("Input the length "))
    width = int(input("Input the width "))
    area = length * width
    print(area)

    
'''
Name of Function: numbercheck
Parameters: value
Return Value: value
What it does: Gets a number with a error check in it.
'''
def numbercheck(value):
    number = -1
    while number < 0:
        try:
            number = int(input(value))
        except ValueError:
            print("This is not a number, please enter again")
    return number

'''
Name of Function: divisoncheck()
Parameters: 
Return Value: 
What it does: It works out x and y by dividing it.
'''
def divisoncheck():
    try:
        x = numbercheck("Enter a number to divide ")
        y = numbercheck("ENter a number to divide by: ")
        print(x/y)
        
    except ZeroDivisionError:
        print("Cannot divide by zero ")
        y = 1


'''
Name of Function: areaRectangle
Parameters: 
Return Value: Area
What it does: Works out the area of the Rectangle with error chatching
'''

def areaRectangle():
    length = -1
    width = -1
    while length < 0:
        try:
            length = int(input("Please enter the length of the rectangle. "))
            while length < 0:
                print("We do not accept negitive numbers! Sorry.")
                length = int(input("Please enter the length of the rectangle. "))
        except:
            print("There was a error somewhere! Please try again.")
    while width < 0:
        try:
            width = int(input("Please enter the width of the rectangle. "))
            while length < 0:
                print("We do not accept negitive numbers! Sorry.")
                length = int(input("Please enter the length of the rectangle. "))
        except:
            print("There was a error somewhere! Please try again.")
    area = length*width
 #   print("Your area is ",  area)
    return area


'''
Name of Function: error4
Parameters: 
Return Value: Number
What it does: Prints square numbers from 1 to 12
'''
def error4():
    number = 1
    while number < 13:
        print(number, "Squared is ", number*number)
        number = number + 1
