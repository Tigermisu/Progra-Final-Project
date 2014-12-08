"""
Mini puzzle - R-Soul
9 Weights, 1 Scale, 2 Movements

Modules Used: Random~
"""
import random
import time

def weightPuzzle(correct):
    options = [1,1,1,1,1,1,1,1,1]
    options[correct-1] = 2
    used = []
    used2 = []
    lefttotal = 0
    righttotal = 0
    done = ""
    chosen = input("I select number... ")
    while done not in ("yes", "Yes", "Y", "y"):
        if done in ("No","no","n","N"):
            options = [1,1,1,1,1,1,1,1,1]
            options[correct-1] = 2
            used = []
            lefttotal = 0
            done = ""
            chosen = input("\nLet's do this again then. I choose number... ")
        while chosen != "0":
            if chosen in ("1","2","3","4","5","6","7","8","9"):
                if options[int(chosen)-1] == "X":
                    chosen = input("Weight already in use, please choose another one. ")
                else:
                    lefttotal += options[int(chosen)-1]
                    used.append(int(chosen))
                    options[int(chosen)-1] = "X"
                    chosen = input("And number... ")
            else:
                chosen = input("Invalid option, please try again. ")
        done = input("You have chosen %s for the left side, is this ok? (Y/N) " % (used))
        while done not in ("Yes","yes","y","Y","No","no","n","N"):
            done = input("Invalid option, please try again. ")
    #REPEAT
    done = ""
    chosen = input("\nAs for the right scale, which weight do you wish to place? ")
    while done not in ("yes", "Yes", "Y", "y"):
        if done in ("No","no","n","N"):
            for numused in used2:
                options[numused-1] = 1
                if numused == correct:
                    options[numused-1] = 2
            used2 = []
            righttotal = 0
            done = ""
            chosen = input("\nLet's do this again then. I choose number... ")
        while chosen != "0":
            if chosen in ("1","2","3","4","5","6","7","8","9"):
                if options[int(chosen)-1] == "X":
                    chosen = input("Weight already in use, please choose another one. ")
                else:
                    righttotal += options[int(chosen)-1]
                    used2.append(int(chosen))
                    options[int(chosen)-1] = "X"
                    chosen = input("And number... ")
            else:
                chosen = input("Invalid option, please try again. ")
        done = input("You have chosen %s for the right side, is this ok? (Y/N) " % (used2))
        while done not in ("Yes","yes","y","Y","No","no","n","N"):
            done = input("Invalid option, please try again. ")
    if righttotal > lefttotal:
        tilt = "The right side was heavier."
    elif lefttotal > righttotal:
        tilt = "The left side was heavier."
    else:
        tilt = "Both sides weight the same."
    print("\nWeights %s were placed on the left side, and %s on the right side.\n%s\n" % (used, used2,tilt))

def foundWeightPuzzle():
    print('It looks as if it hasn\'t been used in ages, or so you thought.')
    time.sleep(3)
    print('Your eyes are attracted by a glittering object hanging on the corner.')
    time.sleep(3)
    print("After getting closer you can appreciate a golden scale with a note:\n")
    time.sleep(3)
    print('"Here are nine weights, they are the same at plain sight, only that one is\nheavier. Your goal is to find that particular one, if you wish what\'s\ninside that is."\n')
    time.sleep(8)
    print('"There is but one restriction, that you may use this scale only twice."')
    time.sleep(3)
    print("\nWhat do you choose?\nA: Give it a try.\nB: Let it be.\n")
    decision = input("I choose... ")
    while decision not in ("a","b","A","B"):
        decision = input("Invalid command. Please choose again... ")
    ### DIDN'T WANT TO DO THE PUZZLE =| ###
    if decision in ("b","B"):
        #### Variable for touching and not doing, or ignore this :p
        print("You leave the contraption untouched.")
        return 3
        
    else:
        correct = random.randint(1,9)
        print('\nUpon closer inspection, you notice there are small numbers on each weight:\n|1| |2| |3| |4| |5| |6| |7| |8| |9|\n\nLet us proceed, which of them do you wish to put on the left side?\nNumber + Enter to select. "0" to finish.\n')
        weightPuzzle(correct)
        print("You have one more movement. Think wisely...")
        weightPuzzle(correct)
        print("You tried moving the scale once more, but it won't budge.")
        time.sleep(3)
        print("The scale reveals a secret chamber, where one weight would barely fit.\nGuess the heaviest goes there?")
        time.sleep(5)
        guess = int(input("Which one do you want to put in?  "))
        confirm = input("Weight #%s is it? (Y/N) " % (guess))
        while confirm not in ("Yes","yes","Y","y"):
            if confirm in ("n","N","No","no"):
                guess = int(input("Then, which one? "))
                confirm = input("Choose weight #%s? (Y/N) " % (guess))
        if guess == correct:
            ### HE GUESSED IT!!! ###
            print("\nYou guessed correctly.\nLight comes in through a hole and illuminates the room.")##ERASE ME
            return True
        else:
            ### NICE TRY ###
            print("\nThe weight is thrown out violently and hits you in the head. You must have guessed wrong.\nLight comes in through a hole and illuminates the room.")##ERASE ME
            return False
