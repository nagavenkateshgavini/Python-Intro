import random

isit = True
while isit:
    num = int(input("Enter the num:"))
    guess = random.randint(0, 10)
    if guess == num:
        print("u won")
        isit = False
    else:
        print("It is not, Do u want to continue")
        gm = input("Enter q or y:")
        if gm == "q":
            isit = False
        else:
            isit = True
        
        
