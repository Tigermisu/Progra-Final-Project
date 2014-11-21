"""
Mini puzzle - Kagynt
lexical number succession
"""

def numSuccession ():
    tried = 0
    lWall = "1:~, 4:4, 2:~, 7:5, 5:4"
    rWall = "3:5, 6:3, 10:3, 12:6, 20:6"
    Wall = "8:_, 11:_, 90:_"
    answer= ["5", "6", "6"]
    query = ["0","0","0"]
    win = False
    lock = False
    print('''You find yourself in a room with no doors or windows\n and what it seems to be letters on the walls''')
    while not win:
        deci = input("What would you like to do?\nA: Walk to the left wall.\nB: Walk to the right wall.\nC: Walk to the front wall.\nD: Walk to the back wall.\n")
        while deci not in ("A", "B", "C", "D", "a", "b", "c", "d"):
            deci = input("Invalid command. Please choose again... \n")
    #Making my way to the Left
        if deci in ("A","a"):
            print("You see a pretty damaged writing in the wall")
            print("You manage to read some numbers along the broken (~) pieces of wall")
            print(lWall)
            deci = input("Press B to go back\n")
            while deci not in ("B", "b"):
                deci = input("Invalid command. Please choose again... \n")
            print("You're back at the center of the room")
    #Making my way to the Right
        elif deci in ("B", "b"):
            print("You see a very well conserved wall")
            print("It seems as if it was part of an archaeological collection.\nThere are some numbers written in it")
            print(rWall)
            deci = input("Press B to go back\n")
            while deci not in ("B", "b"):
                deci = input("Invalid command. Please choose again... \n")
            print("You're back at the center of the room")
    #Now you're looking at the Front
        elif deci in ("C", "c"):
            print("There lies a very ominous-looking gate in front of you, with no apparent handle\nand it seems like not even a hundred men could break it open")
            #Second+ Try
            if Wall != "8:_, 11:_, 90:_":
                deci =input("What would you like to do?\nA: Change the rings.\nB: Push the door\nC: Go back.\n")
            else:
                deci =input("What would you like to do?\nA:Inspect closer.\nB: Push the door\nC: Go back.\n")
            while deci not in ("A", "a","B","b","C","c"):
                deci = input("Invalid command. Please choose again... \n")
            if deci in ("A","a"):
                if tried == 0:
                    print("You find three very small stone rings with numbers engraved on them,\n every single one is below a big faint number on the wall(8, 11 and 90)")
                    print('''Next to the rings, there's a very faint writing on the wall, you squint your eyes and read it....\n"He who attempts to defile the vault, must first overcome the trial of the observant" '''+Wall+'''\nHmmm... perhaps it has something to do with the ring's number?''')
                if not lock:
                    Wall = "8:_, 11:_, 90:_"
                    print(Wall)
                    query[0] = input("So what would you like to set the first ring to? (0-9)\n")
                    while query[0] not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        query[0] = input("Invalid command. Please choose again... \n")
                    Wall = Wall.replace("_", query[0], 1)
                    print(Wall)
                    query[1] = input("What about the second one? (0-9)\n")
                    while query[1] not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        query[1] = input("Invalid command. Please choose again... \n")
                    Wall = Wall.replace("_", query[1], 1)
                    print(Wall)
                    query[2] = input("And the third one? (0-9)\n")
                    while query[2] not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        query[2] = input("Invalid command. Please choose again... \n")
                    Wall = Wall.replace("_", query[2], 1)
                    print(Wall)
                    if query == answer:
                        print("You hear a quiet click and the rings lock in place")
                        lock = True
                    else:
                        print("Nothing seems to happen")
                    deci = input("Press B to go back\n")
                    while deci not in ("B", "b"):
                        deci = input("Invalid command. Please choose again... \n")
                else:
                    print("They're locked")
                    deci = input("Press B to go back\n")
                    while deci not in ("B", "b"):
                        deci = input("Invalid command. Please choose again... \n")
                tried = 1
            elif deci in ("B", "b"):
                if lock:
                    print("The door opens wide almost effortlessly. Congratulations!!")
                    win = True
                else:
                    print("It won't move")
                    deci = input("Press B to go back\n")
                    while deci not in ("B", "b"):
                        deci = input("Invalid command. Please choose again... \n")   
            if not win:    
                print("You're back at the center of the room")

        #This is the back door
        elif deci in ("D","d"):
            print("You find a writing on the floor, it doesn't look like it is part of the initial design of the tomb")
            print('''It says:"Psst psst! Count the first ones!!!"....the first what?''')
            deci = input("Press B to go back\n")
            while deci not in ("B", "b"):
                deci = input("Invalid command. Please choose again... \n")
            print("You're back at the center of the room")
            #
def ringMove(z1, z2):
    opp = {"left":"right", "right":"left"}
    moves = 0
    side = ""
    moves = z2 - z1
    if moves == 0:
        return("You let the ring be.")
    elif moves == 5 or moves == -5:
        return ("You move the ring 5 ticks.")
    elif moves > 5 or moves < -5:
        side = "left"
        if moves < 0:
            moves *=-1
            side = opp[side]
        moves = 10 - moves
    elif moves < 5 and moves > -5:
        side = "right"
        if moves < 0:
            moves*=-1
            side = opp[side]
    return ("You move the ring "+str(moves)+" ticks to the "+side+".")
numSuccession()
#print(ringMove(0, 5))
