"""
Main program
Controls flow, global variables and well... flow.

Stage system is used to control game progess.

Stages 0 through 9 control overall game progress
10 through 19 are the first elevator's puzzle stages
20 through 29 are the second one  stages which may or may not exist
90 is the dead stage in case we want to add something special

Used variables:
stage - determines what part of the game is run
wpuzzle - Luis' weight/scale puzzle. Value is False for failed puzzle, 0 for not done yet.
kpuzzle - Luis' knight puzzle.
rtpuzzle - Ricky's torch puzzle (Actually discs, not torches, whatever.
mpuzzle - Ricky's marble puzzle.
rpuzzle - Pineda's riddle puzzle
tpuzzle -
firstcompletition - 
completed - How many puzzles have been finished, regardless of right or wrong answer.
"""

import saveload
import scaleProblem
import time
import marblePuzzle
import knightsJourney
import Title
import Elevator
import musicWater
import chrisPuzzle
import tokenPuzzle

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
    savestatus['firstcompletition'] = 0
    #3 for not done, since 0 or 1 conflicts with true and false
    savestatus['wpuzzle'] = 3
    savestatus['kpuzzle'] = 3
    savestatus['rtpuzzle'] = 3
    savestatus['mpuzzle'] = 3
    savestatus['rpuzzle'] = 3
    savestatus['tpuzzle'] = 3

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
        print("There is a passage up ahead, do you want to explore?")
        try:
            des = ''
            des = input('Y/N ')
            while des not in "yYnN10" or des == '':
                    print("Invalid input.")
                    des = input('Y/N ')
            if des == 'Y' or des == 'y':
                savestatus['stage'] = 1
                break
            else:
                print("\nYou decide to stay.")
                time.sleep(2)
                print("It is getting cold, do you want to move up?")
                des = input('Y/N ')
                while des not in "yYnN10" or des == '':
                    print("Invalid input.")
                    des = input('Y/N ')
                if des == 'Y' or des == 'y':
                    print("You stand up and make your way down the cave.")
                    savestatus['stage'] = 1
                    break
                else:
                    print("\nIt is comfortable here.")
                    time.sleep(2)
                    print("You fall asleep. A spider walks up your chests and bites you in the heart.")
                    time.sleep(2)
                    print("You're dead.")
                    time.sleep(3)
                    print("Game Over")
                    input("")
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
    while des not in "yYnN10" or des == '':
                    print("Invalid input.")
                    des = input('Y/N ')
    if des == 'Y' or des == 'y':
        print("\nThe water doesn't have any taste, but you feel refreshed.\n")
    time.sleep(2)
    print("You continue walking down the cave and stumble upon a bizarre elevator.\nIt is covered in vines, the chamber is illuminated by glowing mushrooms.")
    time.sleep(2)
    # Pending elevator implementation
    Elevator.daElevaturr()
    savestatus['stage'] = 2
    time.sleep(1)


#Puzzle elevator handling
while (savestatus['stage'] > 9 and savestatus['stage'] < 20) or savestatus['stage'] == 2:

    #Main elevator chamber
    if savestatus['stage'] == 2:
        lights = (savestatus['completed'] if savestatus['completed'] < 1 else savestatus['completed'] - 1) 
        print("There are %s button(s) glowing.\n" % (3 - lights))
        #Path to Luis' puzzle
        print("The 4th button is glowing." if savestatus['kpuzzle'] == 3 else "The 4th button is dark.")
        print("The 6th button is glowing." if savestatus['wpuzzle'] == 3 else "The 6th button is dark.")
        print("The 9th button is glowing." if savestatus['rtpuzzle'] == 3 else "The 9th button is dark.")
        print("" if savestatus['completed'] < 1 else "A numberless button has started to glow.")
        if savestatus['completed'] < 1:##########CAMBIÉ EL MÍNIMO A UNO
            des = input("\nWhich one do you want to press? [4,6,9] ")
            while des not in "469" or des == '':
                print("Invalid input, please choose a button.")
                des = input("\nWhich one do you want to press? [4,6,9] ")
        else:
            des = input("\nWhich one do you want to press? [4,6,9, 0 for the numberless glowing button...] ")
            while des not in "4690" or des == '':
                print("Invalid input, please choose a button.")
                des = input("\nWhich one do you want to press? [4,6,9, 0 for the numberless.] ")
        if des == '6':
            if savestatus['wpuzzle'] == 3:
                savestatus['stage'] = 10
                print("You head for the 6th floor.")
            else:
                print("The elevator doesn't move.")
        elif des == '4':
            if savestatus['kpuzzle'] == 3:
                savestatus['stage'] = 11
                print("You head to the 4th floor.")
            else:
                print("The elevator doesn't move.")
        elif des == '9':
            if savestatus['rtpuzzle'] == 3:
                savestatus['stage'] = 12
                print("You head into the 9th floor.")
            else:
                print("The elevator doesn't move.")
        else:
            savestatus['stage'] = 3
            print("You head... somewhere.")
        time.sleep(2)
    


    #Luis' scale puzzle handling      
    if savestatus['stage'] == 10:
        print("\nThe elevator leaves you on a dark room, you can see webs on the \nfloor and the walls.")
        time.sleep(3)
        #If it is 3, means that the user walked away or has not done it, so he can do it again.
        if savestatus['wpuzzle'] == 3:
            savestatus['wpuzzle'] = scaleProblem.foundWeightPuzzle()
            #If the puzzle was answered, regardless of answer, add one to completition
            if savestatus['wpuzzle'] != 3:
                savestatus['completed'] += 1
        time.sleep(1)
        print("\nYou return to the elevator and head back.\n")
        savestatus['stage'] = 2

    #Luis' knight puzzle
    if savestatus['stage'] == 11:
        print("\nYou come out on a strangely-tidy room, yet empty room.\n\
on the center lays a table with a bright lamp, some books and a chess board.\n\
as you approach the chess board, you can read an inscription on the wood:")
        time.sleep(2)
        input("(Press enter to continue.)")
        while True:
            savestatus['kpuzzle'] = knightsJourney.foundKnightPuzzle()
            if savestatus['kpuzzle'] != 3:
                savestatus['completed'] += 1
                break
            else:
                des = input("Do you want to try again? (Y/N) ")
                while des not in "yYnN10" or des == '':
                    print("Invalid input.")
                    des = input("Do you want to try again? (Y/N) ")
                if des not in "yY1":
                    break
        time.sleep(2)    
        print("\nThere is nothing more of interest here, you return to the elevator.\n")
        savestatus['stage'] = 2

    #Ricky's water puzzle
    if savestatus['stage'] == 12:
        print("The elevator arrives.\n")
        time.sleep(1)
        savestatus['rtpuzzle'] = musicWater.waterRising()
        time.sleep(3)
        if savestatus['rtpuzzle']:
            savestatus['completed'] += 1
            print("As the water drains, you're allowed back into the elevator.")
            time.sleep(2)
            savestatus['stage'] = 2
        else:
            print("You stay for a while, then pass out on the dirty, cold water.")
            time.sleep(2)
            print("You're dead.")
            time.sleep(2)
            print("Game Over")
            input("")
            savestatus['stage'] = 95

    save()

"""
    


    #Pineda's puzzle
    if savestatus['stage'] == 13:
        print("\nThere is nothing more of interest here, you return to the main chamber\n")
        savestatus['stage'] = 2


    #if all puzzles have been done, advance to the next chamber
    if savestatus['completed'] == 4:
        print("As you return to the chamber, a passage opens in the middle,\nyou peek down it and a gust of wind sucks you in")
        savestatus['stage'] = 3

"""

#---------------------#
#   End giant While   #
#---------------------#

if savestatus['stage'] == 3:
    #Saves how many puzzles were completed in the first stage
    #before resetting the counter
    savestatus['firstcompletition'] = savestatus['completed']
    savestatus['completed'] = 0
    print("After a few mintues of movemement, the elevator stops.\n")
    time.sleep(2)
    chrisPuzzle.numbersPuzzle()
    print("You are surprised on what your eyes see: a big, medieval-style hall.")
    time.sleep(2)
    savestatus['stage'] = 20
    save()

    
while savestatus['stage'] >= 19 and savestatus['stage'] < 30:
    if savestatus['stage'] == 20:
        print("The room branches in several roads, not surprising:\n")
        print("A.- A road leading to a closed iron gate." if savestatus['completed'] < 1 else "A.- A path leading to the now open iron gate.")
        print("B.- A path to an open door with a marble-like sign on top." if savestatus['mpuzzle'] == 3 else "B.- The door at the end of the path is closed now.")
        print("C.- A lane that takes to an open door with a vase carved on it." if savestatus['rpuzzle'] == 3 else "C.- The door at the end of the lane is closed now.")
        print("D.- A stroll that has images of tokens on the sides, leading to an open door." if savestatus['tpuzzle'] == 3 else "D.- The door at the end of the stroll is closed now.")
        des = input("Which one do you want to take? [ABCD] ").lower()
        while des not in "abcd":
            des = input("Invalid input, please try again... ")
        if des == "a":
            if savestatus['completed'] < 1:
                print("The door is closed.")
            else:
                savestatus['stage'] = 4
                print("You enter the great iron gate...")
        elif des == 'b':
            if savestatus['mpuzzle'] == 3:
                savestatus['stage'] = 21
                print("You walk across the path... ")
            else:
                print("That door is closed.")
        elif des == 'c':
            if savestatus['rpuzzle'] == 3:
                savestatus['stage'] = 22
                print("You walk across the lane... ")
            else:
                print("That door is closed.")
        elif des == 'd':
            if savestatus['tpuzzle'] == 3:
                savestatus['stage'] = 23
                print("You walk across the stroll... ")
            else:
                print("That door is closed.")
                
    #Aqui pon el texto para decidir a que camino ir, luego pongo
    #la logica de que se abra el camino principal si quieres
    #para regresar aqui es el stage 20
    
    #Dale a cada puzzle un stage del 21 al 30
    #ej: if a:
    #   savestatus['stage'] == 21


    #Ricky's Marble puzzle
    if savestatus['stage'] == 21:
        print("You cross a small stream and head left down a path.\nIt looks like you ended up in a street from London.\n")
        time.sleep(2)
        print("Is this a dream?")
        time.sleep(2)
        print("It's cold and dark, the public lightning are just oil lamps and it look's like\nit's the 1800s.\n")
        time.sleep(4)
        if savestatus['mpuzzle'] == 3:
            savestatus['mpuzzle'] = marblePuzzle.marblePuzzle()
            if savestatus['mpuzzle'] == True:
                savestatus['completed'] += 1
        time.sleep(1)
        print("\nThere is nothing more of interest here, you keep walking down and return\nto the main chamber.\n")
        savestatus['stage'] = 20

    #segundo puzzle:
    if savestatus['stage'] == 22:
        time.sleep(2)
        import waterVases
        savestatus['rpuzzle'] = waterVases.waterVases()
        if savestatus['rpuzzle'] == True:
            savestatus['completed'] += 1
            print("The door opens and you walk back.")
        else:
            print("The door opens and you peacefully walk back to where you came from.")
        savestatus['stage'] = 20

    #tercer puzzle:
    if savestatus['stage'] == 23:
        time.sleep(1)
        print("You reach a dead end when suddenly a heavy gate closes behind you/n preventing your return")
        savestatus['tpuzzle'] = tokenPuzzle.tokenPuzzle()
        if savestatus['tpuzzle'] == True:
            savestatus['completed'] += 1
            print("The door opens and you walk back.")
        else:
            print("The door opens and a mystical force launches you back to the start,\nyou suffer minor wounds in the fall.")
        savestatus['stage'] = 20 
        
    
    #Si pasa cada puzzle, sube savestatus['completed'] += 1
    save()

######################
###END OF WHILE
######################

#Final stage
if savestatus['stage'] == 4:
    time.sleep(2)
    print("You keep walking...")
    time.sleep(2)
    print("It looks like there is no end to this road.")
    time.sleep(2)
    print("\nA light!\n")
    time.sleep(2)
    print("You rush forward into the light but suddenly stop as you notice a pitfall right\nbeneath your feet.")
    time.sleep(3)
    print("You turn around and notice two lightbulbs above you.")
    time.sleep(2)
    savestatus['completed'] += savestatus['firstcompletition']
    if savestatus['completed'] < 5:
        print("However, only one light shines.")
        time.sleep(2)
        print("As you look around, you notice a set of torches turned off.")
        import torchesPuzzle
        torchesPuzzle.torches()
        time.sleep(1)
        print("You solved it!")
        time.sleep(2)
        print("A bridge downs")
    else:
        print("Both are brightly shining, and a small bridge lowers\nto cross into a small room to the right.")
        time.sleep(3)
        print("You cross the bridge and enter the room.")
        time.sleep(3)
        import OneWayKnights
        OneWayKnights.OneWayKnights()
        print("Putting them all into place, something sounds from where you came from")
        time.sleep(2)
        print("You run back and notice a bridge has lowered cross the pitfall.")
        time.sleep(3)
    print("As you cross the deadly trap, you find a mirror. You look into it.")
    time.sleep(5)
    print("You see yourself.")
    time.sleep(3)
    print("What were you expecting?\n")
    time.sleep(3)
    print("You keep walking downa tunnel when a yet brighter light blinds you.")
    time.sleep(3)
    print("Could this be it?")
    time.sleep(2)
    print("You rush yourself, it's sunlight, you found the exit!")
    time.sleep(2)
    #add conclsuion drama here
    print("The landscape you perceive is nothing but beautiful.")
    time.sleep(3)
    print("Worth all the ordeals you just went through.")
    time.sleep(3)
    print("Vast mountains, bountiful lakes and rivers.")
    time.sleep(3)
    print("Countless flora and fauna abound.")
    time.sleep(3)
    print("Finally, you got to see this new bright world.")
    input("\nThank you for playing!")
    
d = 0
while savestatus['stage'] >= 90:
    time.sleep(10)
    print("You're dead, what are you waiting for?")
    time.sleep(4)
    print("The wait is eternal, never-ending.")
    time.sleep(4)
    print("If an immortal astronaut floats away from his ship, is he condemned to never stand again?")
    des = input("[Y/N] ")
    time.sleep(3)
    d += 1
    if d > 0:
        print("According to the concept of infinity, he will eventually reach a planet exactly like earth.")
        time.sleep(3)
        print("According to the same theory, you wil live again as long as you keep waiting.")
        time.sleep(3)
        print("Good luck.")
        d = -2**99
        input("\nThank you for playing!")

    
