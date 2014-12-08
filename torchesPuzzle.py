'''
Mini puzzle - R-Soul

Direct answer = B2 > D3 > E5 > C4 > E4 > A3 > B4 > E1 > C1 > A1 > D2
'''
import time

color = {0:"-",1:"O",2:"X"}
def printboard(board):
    print("\n    [A] [B] [C] [D] [E]\n    -------------------\n[1] |%s| |%s| |%s| |%s| |%s|\n    -------------------\n[2] |%s| |%s| |%s| |%s| |%s|\n    -------------------\n[3] |%s| |%s| |%s| |%s| |%s|\n    -------------------\n[4] |%s| |%s| |%s| |%s| |%s|\n    -------------------\n[5] |%s| |%s| |%s| |%s| |%s|\n    -------------------\n" % (color[(board[0]%3)],color[(board[1]%3)],color[(board[2]%3)],color[(board[3]%3)],color[(board[4]%3)],color[(board[5]%3)],color[(board[6]%3)],color[(board[7]%3)],color[(board[8]%3)],color[(board[9]%3)],color[(board[10]%3)],color[(board[11]%3)],color[(board[12]%3)],color[(board[13]%3)],color[(board[14]%3)],color[(board[15]%3)],color[(board[16]%3)],color[(board[17]%3)],color[(board[18]%3)],color[(board[19]%3)],color[(board[20]%3)],color[(board[21]%3)],color[(board[22]%3)],color[(board[23]%3)],color[(board[24]%3)]))

def torches():
    print('\nMake all the lanterns shine green! An omnipotent voice yells.')
    time.sleep(3)
    print('If you select one, the adjascent ones will change:')
    time.sleep(3)
    print("Only diagonals won't change with the adjascents.\n")
    time.sleep(3)
    print("The sequence is: Green > Red > Blue > Green\n")
    time.sleep(3)
    print("Or - > O > X > -\n\n- = Green\nO = Red\nX = Blue\n\n")
    time.sleep(3)
    print('You can select a coordinate [A1] or "reset" the game.')
    time.sleep(3)
    
    board = [2,0,2,0,2,0,2,0,1,1,2,0,1,1,1,1,1,1,0,1,0,2,2,2,1]
    first = {"a":1, "A":1, "b":2, "B":2, "c":3, "C":3, "d":4, "D":4, "e":5, "E":5}
    result = 1
    while result > 0:
        printboard(board)
        option = input("Please select a coordinate. [A1] ")
        while option not in ("reset", "Reset", "A1", "a1", "B1", "b1", "C1", "c1", "D1", "d1", "E1", "e1", "A2", "a2", "B2", "b2", "C2", "c2", "D2", "d2", "E2", "e2", "A3", "a3", "B3", "b3", "C3", "c3", "D3", "d3", "E3", "e3", "A4", "a4", "B4", "b4", "C4", "c4", "D4", "d4", "E4", "e4", "A5", "a5", "B5", "b5", "C5", "c5", "D5", "d5", "E5", "e5"):
            option = input ("Invalid coordinate, please try again... ")
        if option in ("reset", "Reset"):
            board = [2,0,2,0,2,0,2,0,1,1,2,0,1,1,1,1,1,1,0,1,0,2,2,2,1]
            print("The board has been reset.")
        else:
            pos = (first[option[0]]+(int(option[1])-1)*5)-1
            board[pos] += 1
            if (pos+1) % 5 == 0:
                pass
            else:
                board[pos+1] += 1
            if (pos+1) % 5 == 1:
                pass
            else:
                board[pos-1] += 1
            if (pos+1) <= 5:
                pass
            else:
                board[pos-5] += 1
            if (pos+1) >= 21:
                pass
            else:
                board[pos+5] += 1
        result = 0
        for num in board:
            result += (num%3)
    if result == 0:
        return True
        
if __name__ == "__main__":
    torches()
    
