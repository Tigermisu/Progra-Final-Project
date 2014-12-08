"""
Chris' math puzzle.
Because I had to.
"""
from time import sleep


def intro():
    print("The room is covered in gears and rusted steam machinery.")
    sleep(2)
    print("After a quick look, you notice a big bronze door in your path.")
    sleep(2)
    print("You try to open it but it won't budge.")
    sleep(2)
    print("After a few hard kicks rust falls off releaving an inscription:\n")
    print("'The natural numbers below 10 that are multiple of 3 or 5 are 3, 5, 6 and 9.\nThe sum of these multiples is 23.'\n")
    sleep(5)
    print("Odd.\n")
    sleep(2)
    print("Looking around some more you find a dial near the hinge of a door. It reads:\n'What is the sum of all multiples of 3 or 5 below 1000?'")
    sleep(5)
    print("\nAs you touch the dial, several machinery appear to start working around you.")
    sleep(5)

def decide():
    print("\nWhat do you want to do next?")
    print("A: Try to input a number into the dial.")
    print("B: Operate the giant calculator.")
    print("C: Tinker with the sum machine.")
    print("D: Use the modulo module.")
    x = input("Choose an option: ")
    while x not in "AaBbCcDd" or x == '':
        print("Invalid input.")
        x = input("Choose an option: ")
    return x.lower()

def tryopen():
    print("\nThere are six dials.")
    dials = [0,0,0,0,0,0]
    print(dials)
    print("\nWhat would you want to set the first dial to?")
    for x in range(6):
        ds = input("Enter a number: ")
        while ds not in "1234567890" or ds == '':
            print("Invalid Input")
            ds = input("Enter a number: ")
        dials[x] = int(ds)
        print("")
        print(dials)
        print("")
        if x != 5:
            print("What would you like to set the next number to?")
        else:
            print("")
    sleep(1)
    print("You hear a few clicks")
    sleep(2)
        
    if dials == [2, 3, 3, 1, 6, 8]:
        #233168
        print("The door opened!")
        return True
    print("The door remains closed.")
    return False
    
def calculator(ans):
    n1 = input("Enter the first number, or enter 'a' for the previous answer: ")
    while True:
        try:
            n1 = int(n1)
            break
        except:
            if n1 == 'a':
                break
            print("Invalid input.")
            n1 = input("\nEnter the first number, or enter 'a' for the previous answer: ")
    op = input("Enter an operator from the list: * / + - % ")
    while op not in '*/+-%' or op == '':
        print("Invalid Input")
        op = input("Enter an operator from the list: * / + - % ")
    n2 = input("Enter the second number, or enter a for the previous answer: ")
    while True:
        try:
            n2 = int(n2)
            break
        except:
            if n2 == 'a':
                break
            print("Invalid input.")
            n2 = input("Enter the second number, or enter 'a' for the previous answer: ")
    if (n1 == 'a' or n2 == 'a') and ans == '':
        print("No previous answer found in memory. Try again")
        calculator('')
    else:
        if n1 == 'a':
            n1 = ans
        if n2 == 'a':
            n2 = ans
        newans = eval(str(n1) + op + str(n2))
        print("%s appears on the dusted screen." % (newans))
        des = input("\nWould you like to do another operation? Y/N ")
        while des not in 'YyNn1' or des == '':
            print("Invalid input")
            des = input("\nWould you like to do another operation? Y/N ")
        if des in "Yy1":
            calculator(newans)
        else:
            print("As you walk away, the machine clears its memory.")
            sleep(2)

def summachine(mod):
    if mod == None:
        nums = []
        while True:
            print("Input a number, type anything else to stop.")
            nu = input("Choose a number: ")
            try:
                nums.append(float(nu))
            except:
                break
        print("%s appears on the rusted screen" % (sum(nums)))
        des = input("\nWould you like to do another operation? Y/N ")
        while des not in 'YyNn1' or des == '':
            print("Invalid input")
            des = input("\nWould you like to do another operation? Y/N ")
        if des in "Yy1":
            summachine(None)
    
def modulo():
    print("As you approach the machine, it appears to be directly linked\nto the sum machine.")
    n1 = input("Enter the base number: ")
    while True:
        try:
            n1 = int(n1)
            break
        except:
            print("Invalid input.")
            n1 = input("Enter the base number: ")
    n2 = input("Enter the number of multiples you want: ")
    while True:
        try:
            n2 = int(n2)
            break
        except:
            print("Invalid input.")
            n2 = input("Enter the number of multiples you want: ")
    x = 0
    y = 1
    numbers = []
    while x < n2:
        if y % n1 == 0:
            numbers.append(y)
            x += 1
        y += 1
    print("\nThe machine starts working. Loud mechanical noises torment your ears.")
    sleep(4)
    print("A strip of numbers comes out.\n")
    sleep(3)
    while True:
        print("What do you want to do?\nA:Look at the strip.\nB:Input the strip into the sum machine\nC:Input another modulo operation\nD:Walk away.")
        x = input("I choose... ")
        while x not in "AaBbCcDd" or x == '':
            print("Invalid input.")
            x = input("Choose an option: ")
        if x.lower() == 'a':
            print(numbers)
            sleep(3)
        elif x.lower() == 'b':
            print("You insert the strip in a slot, after a few seconds a number is printed:\n%s\n" % (sum(numbers)))
            sleep(3)
        elif x.lower() == 'c':
            modulo()
            return
        else:
            print("As you walk away, the strip of paper is blown away by a gust of wind")
            sleep(2)
            return
        


def numbersPuzzle():
    intro()
    opened = False
    while not opened:
        d = decide()
        if d == 'a':
            opened = tryopen()
        elif d == 'b':
            print("\nThis is an old, really un-intuitive calculator.")
            calculator('')
        elif d == 'c':
            print("\nThis machine sums all numbers that you put in it.")
            summachine(None)
        else:
            print("\nThis machine prints a list of numbers that are divisible by another")
            modulo()
        

if __name__ == '__main__':
    numbersPuzzle()
