"""
Made by: R-Soul :D
"""
import time

def printtemplate(space):
    print("\n|1|2|3|4|5|6|7|\n|%s|%s|%s|%s|%s|%s|%s|" % (space[0],space[1],space[2],space[3],space[4],space[5],space[6]))

def OneWayKnights():
    print("Upon entering, your sight is mesmerized by an outside garden.")
    time.sleep(2)
    print("The walls are high, and covered with a thorned creeper.")
    time.sleep(3)
    print("Figures, else you would've just jumped.\n")
    time.sleep(3)
    print("You start to walk around and stumble across six giant statues.")
    time.sleep(3)
    print("Three of them are facing to the right, while the rest to the left.")
    time.sleep(4)
    print("They are all lined up perfectly in a stone path.")
    time.sleep(3)
    print("The stone tablet next to them caughts your eyes.\n")
    time.sleep(3)
    print('"We can move the moment you ask us to, but keep in mind:')
    time.sleep(3)
    print('1.- We may only move to the direction we are facing.\n2.- We can only move up to two steps forward.\n3.- To move one step forward, nobody has to be infront.\n4.- To move two steps, someone must be infront, and nobody on the space that\nfollows."')
    time.sleep(10)
    print('\n"We on the right wish to be on the left,\nwhile the ones on the left wish to be on the right."\n')
    time.sleep(6)
    
    print("The statues are aligned... \nFacing to the right [R] and to the left [L].")
    space = ["R","R","R"," ","L","L","L"]
    printtemplate(space)
    time.sleep(3)
    num = input("\nTime to choose one to move I guess...\nYou chose the statue on space... [1-7] ")
    while num not in ("1234567"):
        num = input("Invalid input, please try again... ")
    while True:
        if num in ("1234567"):
            num = int(num)
        if str(num) in "rR":
            space = ["R","R","R"," ","L","L","L"]
            print("\nEverything is now back in place")
            printtemplate(space)
        elif space[num-1] == "R" and num != 7:
            if space[num] == " ":
                space[num] = "R"
                space[num-1] = " "
                printtemplate(space)
                ### Right and one
            elif (space[num] not in (" ")) and space[num+1] == " ":
                space[num+1] = "R"
                space[num-1] = " "
                printtemplate(space)
                ## Right and two
            else:
                print("\nI can't move.")
                printtemplate(space)
                ##Right and none
        elif space[num-1] == "L" and num != 1:
            if space[num-2] == " ":
                space[num-2] = "L"
                space[num-1] = " "
                printtemplate(space)
                ### Right and one
            elif (space[num-2] not in (" ")) and space[num-3] == " ":
                space[num-3] = "L"
                space[num-1] = " "
                printtemplate(space)
                ## Right and two
            else:
                print("\nI can't move.")
                printtemplate(space)
                ##Right and none            
        else:
            print("Impossible movement.")
            printtemplate(space)
        if space == ["L","L","L"," ","R","R","R"]:
            break
        num = input('\nNow let\'s move statue #... [1-7 or "R"] ')
        while num not in ("1234567rR"):
            num = input("Invalid input, please try again... ")
        
    ### PUT WHAT HAPPENS WHEN CLEAR HERE
    print("Clear")

if __name__ == "__main__":
    OneWayKnights()
