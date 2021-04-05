'''
Function Name: flowChart()
Parameters: N/A
Return Value:
What it does:
'''
def flowChart():
    age = input("Please input how old you are -> ")
    gender = input("Please input your gender -> ")
    if int(age) < 20:
        dose = float(age) * 0.1
    else:
        dose = 2
    if gender.lower() == "female":
        isPregnant = input("Are you pregnant? ")
        acceptable = ["True", "Yes", "true", "yes"]
        if isPregnant in acceptable:
            dose = 1.5
    else:
        dose = float(dose) * 0.5

    #print(dose) # Used for debug
