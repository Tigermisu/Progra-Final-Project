"""
Mini puzzle - Kagynt
Correct order with timer
"""
import time

def getBoard (l):
    board = {"a":"OFF", "b":"OFF", "c":"OFF", "d":"OFF"}
    for x in l:
        if l[x] != 0:
            board[x] = "Playing"
        else:
            board[x] = "Silent "
    return("\n-------------------\n|%s| |%s|\n-------------------\n|%s| |%s|\n-------------------\n" % (board["a"], board["b"], board["c"], board["d"]))
    
def waterRising ():   
    print('''As soon as you cross the door, it closes,\nleaving you in a seemingly airtight room.\n''')
    time.sleep(4)
    print('''There's a small slab in the center of the room which reads:\n"Make haste to find your way through darkness\nor time itself will swallow you whole"\n''')
    time.sleep(5)
    print("As soon as you finish reading, the floor shifts\nand the slab goes into it as 4 tall disc players\nin a square pattern emerge in the room\n")
    time.sleep(5)
    print('''A voice is heard rumbling around:\n"Each player contains an instrument of a particular melody..."\n''')
    time.sleep(4)
    print('''"...all 4 of them must be playing in order to advance,\nbut some of them may have a quite long or short winding capacity..."\n''')
    time.sleep(5)
    print('''"...I think you may have 1 or 2 minutes before you drown....Good luck."\n''')
    time.sleep(3)
    tmp = input("Press Enter to begin the puzzle\n")
    for x in range (5, 0, -1):
        #Countdown
        print(x)
        time.sleep(1)
    print("GO!\n")
    print("Water beings to come out of the walls!!\nHurry or it will get to the disc players!!!!!")
    lenghtTorches = {"a":2, "b":4, "c":3, "d":1}
    actualTorches = {"a":0, "b":0, "c":0, "d":0}
    time.clock()
    while time.clock() < 60:
        a = 60-int((time.clock()//1))
        deci = (input("Which player do you want to wind?   |   Time Left: "+str(a)+" seconds.\nA: Torch A.\nB: Torch B.\nC: Torch C.\nD: Torch D.\n")).lower()
        while deci not in ("a","b","c","d"):
            deci = (input("Invalid command. Please choose again... \n")).lower()
        for x in actualTorches:
            #Torches be dying
            if actualTorches[x] != 0:
                actualTorches[x] -= 1
        actualTorches[deci] = lenghtTorches[deci]
        print(getBoard(actualTorches))
        for x in actualTorches:
            if (actualTorches[x]) == 0:
                win = False
                break
        else:
            win = True
            break
    else:
        #Lost
        print("The water level got to the players. It looks like you're\ntrapped here forever.")
        return False
    if win:
        #Won
        print("The water stops rising.")
        return True

if __name__ == '__main__':
    waterRising()

