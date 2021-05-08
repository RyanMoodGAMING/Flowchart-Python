
# My geography quiz
# By Ryan McAllister

def Q1():
    print("Welcome to the georaphy quiz.")
    print("You are not allowed to use google.")
    print()
    print("Question 1: What is the capital of England?")
    print("A) Manchester")
    print("B) Liverpool")
    print("C) London")
    answer = input("Please enter A, B or C as your answer.")
    if answer == "A":
         print("Incorrect! The right answer was London.")
    elif answer == "B":
        print("Incorrect! The right answer was London.")
    else:
        print("Well done. You answer (C) was correct.")

def Q2():
    print()
    print("Question 2: What is the population of England?")
    print("A) 5.32 million people.")
    print("B) 54.79 million people.")
    print("C) 10.47 thousand people")
    answer = input("Please enter A, B or C as your answer.")
    if answer == "A":
         print("Incorrect! The right answer was 54.79 million people.")
    elif answer == "B":
        print("Well done. You answer (B) was correct.")
        print("The population of England is 54.79 million people.")
    else:
        print("Incorrect! The right answer was 54.79 million people.")


def Q3():
    print()
    print("Question 3: What is the population of Hartlepool in 2011?")
    print("A) 92,028 people.")
    print("B) 65,650 people.")
    print("C) 2,000 people")
    answer = input("Please enter A, B or C as your answer.")
    if answer == "A":
         print("Well done. You answer (A) was correct, 92,028 people live there.")
    elif answer == "B":
        print("Incorrect! The right answer was 92,028 people.")
    else:
        print("Incorrect! The right answer was 92,028 people.")

def Q4():
    print()
    print("Question 4: What is the capital of France?")
    print("A) Paris")
    print("B) Hartlepool")
    print("C) Madrid")
    answer = input("Please enter A, B or C as your answer.")
    if answer == "A":
         print("Well done. You answer (A) was correct")
    elif answer == "B":
        print("Incorrect! The right answer is Paris. Hartlepool is in England and isn't a captial.")
    else:
        print("Incorrect! The right answer is Paris.")

def Q5():
    print()
    print("Question 5: What is deforistation?")
    print("A) Were people look after the animals, trees and habitats.")
    print("B) Were people kill animals.")
    print("C) Were people cut down trees, animals die and habitats are destroyed.")
    answer = input("Please enter A, B or C as your answer.")
    if answer == "A":
         print("Incorrect! The right answer was C. It would be nice if this was the answer.")
    elif answer == "B":
        print("Incorrect, the right answer was C. Is it just me or it isn't as bad as C.")
    else:
        print("Correct! Sadly it is happening alot.")

def Q6():
    print()
    print("Question 6: What is the captial of Wales?")
    print("A) Cardif.")
    print("B) London")
    print("C) Billingham")
    answer = input("Please enter A, B or C as your answer.")
    if answer == "A":
         print("Correct! Cardif is the captial of Wales in England.")
    else:
        print("Incorrect. The right answer is Cardif.")

def Q7():
    print()
    print("Question 7: What is the capital of Italy?")
    print("A) Europe")
    print("B) Rome")
    print("C) New York")
    answer = input("Please enter A, B or C as your answer.")
    if answer == "B":
         print("Correct! Rome is the captial of Italy.")
    else:
        print("Incorrect. The right answer is Rome.")
def Q8():
    print()
    print("Question 8: What is the largest river in the world?")
    print("A) Nile river")
    print("B) Amazon River")
    print("C) River Tyne")
    answer = input("Please enter A, B or C as your answer.")
    if answer == "A":
         print("Correct! The Nile River is the largest river in the world")
    else:
        print("Incorrect. The right answer was Nile River.")


def Q9():
    print()
    print("Question 9: What is the largest tower in the world?")
    print("A) Eiffel Tower")
    print("B) Tower of London")
    print("C) Burj Khalifa")
    answer = input("Please enter A, B or C as your answer.")
    if answer == "C":
         print("Correct! I didnt't know this was a tower at first.")
    else:
        print("Incorrect. The right answer was Burj Khalifa.")

def Q10():
    print()
    print("Question 10: Were is the captial of Spain")
    print("A) Madrid")
    print("B) Granada")
    print("C) Mallorca")
    answer = input("Please enter A, B or C as your answer.")
    if answer == "A":
         print("Correct! Well done.")
    else:
        print("Incorrect. The right answer was Madrid.") 

def End():
    print("Well done, you completed the quiz.")
    print("You got UNKNOWMN/10")

Q1()
Q2()
Q3()
Q4()
Q5()
Q6()
Q7()
Q8()
Q9()
Q10()

End()
