
# starter program week 6

#while loop

def bored():
    answer = input("Are you bored? ")
    while answer != "y":
        answer = input("Are you bored yet? N or Y. ")
    print("Got to you in the end!")

bored()


