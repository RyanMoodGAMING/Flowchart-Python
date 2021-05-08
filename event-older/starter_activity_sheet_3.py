# starter program week 3


def cooking():
    print("Meal planner")
    print()
    print("1. Chicken curry.")
    print("2. Chips & Gravy.")
    print("3. Pizza and Chips.")
    print("4. None of the above.")
    print()
    print("Which of these meals is your favourite? (1, 2, 3 or 4) ")
    answer = input()
    if answer == "1":
        print("Chicken curry coming up")
    elif answer == "2":
        print("Chips and gravy coming up")
    elif answer == "3":
        print("Pizza and chips coming up!")
    else:
        print("Ok, maybe you like something else?")
    print("Enjoy!")
    
     
    
cooking()

