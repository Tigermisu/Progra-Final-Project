"""
Mini puzzle - R-Soul
Move a knight chess piece across all the board without repeating cells.

Modules Used: None :D

One of the possible answers can be found at: http://professorlayton2walkthrough.blogspot.mx/2008/11/puzzle107.html
"""
import time

def printboard(board):
    print("-------------------\n|%s| |%s| |%s| |%s| |%s|\n-------------------\n|%s| |%s| |%s| |%s| |%s|\n-------------------\n|%s| |%s| |%s| |%s| |%s|\n-------------------\n|%s| |%s| |%s| |%s| |%s|\n-------------------\n|%s| |%s| |%s| |%s| |%s|\n-------------------\n|%s| |%s| |%s| |%s| |%s|\n-------------------\n" % (board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9],board[10],board[11],board[12],board[13],board[14],board[15],board[16],board[17],board[18],board[19],board[20],board[21],board[22],board[23],board[24],board[25],board[26],board[27],board[28],board[29]))

def options(pieces):
    global board
    options = 0
    for pos in range(0,30):
        if pieces[pos] == "K":
            for pos2 in (-1,1):
                for pos3 in (-2,2):
                    if (int(pos/5) + pos2) < 0  or (int(pos/5) + pos2) > 5 or (pos%5 + pos3) < 0 or (pos%5 + pos3) > 4:
                        pass
                    else:
                        if pieces[pos + (pos2*5)+pos3] != "O":
                            options += 1                        
                            pieces[pos+(pos2*5)+pos3] = str(options)
            for pos2 in (-2,2):
                for pos3 in (-1,1):
                    if (int(pos/5) + pos2) < 0  or (int(pos/5) + pos2) > 5 or (pos%5 + pos3) < 0 or (pos%5 + pos3) > 4:
                        pass
                    else:
                        if pieces[pos + (pos2*5)+pos3] != "O":
                            options += 1                        
                            pieces[pos+(pos2*5)+pos3] = str(options)
    return options

def movement(option,board,number):
    condition = True
    while condition:
        while option not in ("1","2","3","4","5","6","7","8"):
            option = input("Invalid option, please try again. ")
        if int(option) <= 0 or int(option) > number:
            option = input("Invalid option, please try again. ")
        else:
            condition = False
    for pos in range(0,30):
        if board[pos] == "O":
            pass
        elif board[pos] == "K":
            board[pos] = "O"
        elif board[pos] == option:
            board[pos] = "K"
        else:
            board[pos] = "-"
    

def knightJourney():
    board = ["K","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
    movements = 0
    curOptions = 0
    while movements <= 28:
        curOptions = options(board)
        if curOptions == 0:
            break
        printboard(board)
        movement(input("Which number do you wish to move to? "),board,curOptions)
        movements += 1
        print("Only %s space(s) left!\n" % (29-movements))
    if movements == 29:
        ####You made it
        print("You made it!")
        return True
        
    else:
        ####You suck
        print("You are out of moves, you managed %s out of 29." % (movements))
        return 3
        

def foundKnightPuzzle():
    print("\n'The knight wishes to travel along the world, but only\nvisiting every place once.'\n")
    time.sleep(3)
    print('The knight is a chess piece that can only move in "L" shape.\nIt is represented by the symbol "K" on the board.\nThe numbers, represent your possible movements.\nYou must travel each cell of the board only once.\n')
    time.sleep(5)
    return knightJourney()

if __name__ == '__main__':
    knightJourney()
    


