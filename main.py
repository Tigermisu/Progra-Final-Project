"""
Main program
Controls flow, global variables and well... flow.

Stage system is used to control game progess.

Stages 0 through 9 control overall game progress
10 through 19 are puzzle stages
20 through 29 are uncategorized stages which may or may not exist
90 is the dead stage in case we want to add something special

Used variables:
stage - determines what part of the game is run
wpuzzle - Luis' weight/scale puzzle. Value is False for failed puzzled, 0 for not done yet.
mpuzzle - Ricky's marble puzzle.
completed - How many puzzles have been finished, regardless of right or wrong answer.
"""

import saveload
import scaleProblem
import time
import marblePuzzle
import knightsJourney
import Title

#Saves the game, got tired of copy pasting it all over the place
def save():
    print("\nAutosaving")
    time.sleep(1)
    saveload.saveGame(savestatus)
    print('\n')

#Sets all variables to their starting values
def initGame():
    savestatus['stage'] = 0
    savestatus['completed'] = 0
    #3 for not done, since 0 or 1 conflicts with true and false
    savestatus['wpuzzle'] = 3
    savestatus['mpuzzle'] = 3

savestatus = {}

print("Hello, would you like to load or start a new game?")
print("1. New game")
print("2. Load")
while True: 
    try:
        des = int(input("Enter a number: "))
        if des == 1:
            initGame()
            break
        elif des == 2 and saveload.checkSave():
            savestatus = saveload.loadGame()
            break
        elif des == 2 and not saveload.checkSave():
            print("No save file found, starting new game.\n")
            initGame()
            break
        else:
            print("Invalid input, please enter 1 for new game, 2 for load.\n")
    except Exception: 
        print("Invalid input, please enter 1 for new game, 2 for load.\n")
        
print('\nAutosave enabled\n')
time.sleep(1.5)


if savestatus['stage'] == 0:
    print("You wake up in a mysterious cave. It's dark.")
    time.sleep(2)
    print("You look at your feet, your hands, your limbs. You seem fine.")
    time.sleep(2)
    print("You try to recall what happened before this.")
    time.sleep(4)
    print("")
    print("Nothing.")
    time.sleep(3)
    while True:
        print("You're a young kid in an unknown cave. There is a passage up ahead,\ndo you want to explore?")
        try:
            des = ''
            des = input('Y/N ')
            if des == 'Y' or des == 'y':
                savestatus['stage'] = 1
                break
            else:
                print("\nYou decide to stay.")
                time.sleep(2)
                print("You notice a small crevice in the wall.\nIt looks like you can squeeze through it, do you want to?")
                des = input('Y/N ')
                if des == 'Y' or des == 'y':
                    print("It's tight but you managed to make your way through.")
                    savestatus['stage'] = 10
                    break
                else:
                    print("\nIt is comfortable here.")
                    time.sleep(2)
                    print("You fall asleep. A spider walks up your chests and bites you in the heart.")
                    time.sleep(2)
                    print("You're dead.")
                    savestatus['stage'] = 90
                    break
        except Exception:
            print ("Invalid input, try again")


if savestatus['stage'] == 1:
    save()
    print("As you walk down the hill the rocks beneath your feet collapse,\nyou fall a short distance but suffer no harm. There's just no going back")
    time.sleep(2)
    print("There is a small pond with water, do you want to drink?")
    des = input('Y/N ')
    if des == 'Y' or des == 'y':
        print("The water doesn't have any taste, but you feel refreshed.")
    time.sleep(2)
    print("You continue walking down the cave and descend into a chamber,\nsunlight illuminates the cave through a hole in the ceiling")
    time.sleep(2)
    print("You see 4 small paths on the walls of the cave\n\n")
    savestatus['stage'] = 2
    time.sleep(1)


#Puzzle chamber handling
while (savestatus['stage'] > 9 and savestatus['stage'] < 20) or savestatus['stage'] == 2:


    #Main puzzle chamber
    if savestatus['stage'] == 2:
        print("There are 4 arches over each small path\n")
        #Path to Luis' puzzle
        print("The first path is dark." if savestatus['wpuzzle'] == 3 else "A strong light comes from the path, you have finished the puzzle.")
        print("The second path is dark.")
        print("The third path is dark.")
        print("The fourth path is dark.")
        des = input("\nWhich one do you want to traverse? (1,2,3,4) ")
        while des not in "1234":
            print("Invalid input, please choose a path from 1 through 4.")
            des = input("Which one do you want to traverse? (1,2,3,4) ")
        if des == '1':
            savestatus['stage'] = 10
            print("You head down the first path")
        elif des == '2':
            savestatus['stage'] = 11
            print("You head down the second path")
        elif des == '3':
            savestatus['stage'] = 12
            print("You head down the third path")
        else:
            savestatus['stage'] = 13
            print("You head down the fourth path")
        
        
        


    #Luis' scale puzzle handling      
    if savestatus['stage'] == 10:
        print("You walk for a while and end up in the apex of a mountain, \nthe sky is clouded and you see city lights afar.")
        time.sleep(1)
        #If it is 3, means that the user walked away or has not done it, so he can do it again.
        if savestatus['wpuzzle'] == 3:
            savestatus['wpuzzle'] = scaleProblem.foundWeightPuzzle()
            #If the puzzle was answered, regardless of answer, add one to completition
            if savestatus['wpuzzle'] != 3:
                savestatus['completed'] += 1
        time.sleep(1)
        print("\nThere is nothing more of interest here, you return to the main chamber\n")
        savestatus['stage'] = 2

    #Homero's puzzle
    if savestatus['stage'] == 11:
        print("\nThere is nothing more of interest here, you return to the main chamber\n")
        savestatus['stage'] = 2

    #Ricky's Marble puzzle
    if savestatus['stage'] == 12:
        print("You cross a small stream and head left down a path.\nIt looks like you ended up in a street from London.\nIt's cold and dark, the public lightning are just oil lamps and it look's like\nit's the 1800s.\n")
        time.sleep(5)
        if savestatus['mpuzzle'] == 3:
            savestatus['mpuzzle'] = marblePuzzle.marblePuzzle()
            #If the puzzle was answered, regardless of answer, add one to completition
            if savestatus['mpuzzle'] != 3:
                savestatus['completed'] += 1
        time.sleep(1)
        print("\nThere is nothing more of interest here, you keep walking down and return\nto the main chamber.\n")
        savestatus['stage'] = 2

    #Pineda's puzzle
    if savestatus['stage'] == 13:
        print("\nThere is nothing more of interest here, you return to the main chamber\n")
        savestatus['stage'] = 2


    #if all puzzles have been done, advance to the next chamber
    if savestatus['completed'] == 4:
        print("As you return to the chamber, a passage opens in the middle,\nyou peek down it and a gust of wind sucks you in")
        savestatus['stage'] = 3
        
    #Save the game before looping/finishing
    save()

#---------------------
#   End giant While
#---------------------

if savestatus['stage'] == 3:
    time.sleep(2)
    print("You hit your head on the way, but it seems like you're no longer in a cave. \nIt sounds like a plane.")
    time.sleep(2)
    print("\nYep, you're in a plane.\n")
    time.sleep(2)
    print("There are no windows or doors however, just a chess board in front of you.")
    des = ''
    while des != "Y" or des != "y":
        print("Do you want to approach it? (Y/N) ")
        des = input('')
        if des == 'Y' or des == 'y':
            break
        print("Some time passes.")
        time.sleep(2.5)
        print("The board is still there.")
        
    print("You slowly walk near it, noticing a inscription on the table\n")
    time.sleep(1.5)
    knightsJourney.foundKnightPuzzle()
    ####PENDING PROPER PUZZLE IMPLEMENTATION
    
