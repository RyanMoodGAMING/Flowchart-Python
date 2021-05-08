
def message():
    message = input("Enter a message: ")
    repeated = int(input("How many times?: "))
    for i in range(repeated):
        print(message)

def timesTable():
    num = int(input("Enter a number: "))
    for i in range(1,11):
        print(i*num)

def powerOf():
    num = int(input("Enter a number: "))
    if num => 5
        for i in range(1,5):
            print(num**i)

def main():
    choice = ""
    while choice !="4":
        print("1. Message Repeater")
        print("2. Times Table")
        print("3. Power Of")
        print("4. Exit")
        print("Enter your choice:  ")
        choice = input()
        if choice=="1":
            message()
        elif choice=="2":
            timesTable()
        elif choice=="3":
            powerOf()
        print("Goodbye")

def main():
    




#main()
