"""
Mini puzzle - Homeroid
5 tokens on my hand
"""
import time

def tokenPuzzle():
    x = 0
    print("Just as you enter a voice yells at you.\n")
    time.sleep(2)
    play = input('''"Would you like to hear my riddle?"\nA: Ok, tell me!\nB: I think I'll pass.\n''')
    while play not in ("A", "B", "a", "b"):
        play = input("Invalid command. Please choose again... \n")
    if play in ("B, b"):
        print('''Next time it'll be then.''')
        time.sleep(2)
       return 3
    #Aqui empieza
    else:
        print ("\nOkay let's play")
        print ('''"I have X tokens in my hand the there is five types of tokens: \nRed(R), Black(B), Yellow(Y), White(W) and Green(G)"''')
        time.sleep(6)
        print ("\nIf all my tokens are R but six,\nAll my tokens are G except five\nAll tokens W except five and the rest are B and Y.\n")
        time.sleep(6)
        print ("[Note, each token only has one color]")
        answerToken = input('''\nA: R G G W W B Y(7) \nB: R R G B W Y(6) \nC: R G G W B Y Y (7) \nD: R G W B Y(5)\nHow many tokens do I have in my hand and in which quantities? ''')
        while answerToken.lower() not in ("abcd"):
            answerToken = input("Invalid command. Please choose again... \n")
        if answerToken in ("Bb"):
            print('"I\'m sorry but you are wrong."')
            time.sleep(2)
            print("You hear as you exit the room.")
            time.sleep(2)
            return False
        if answerToken in ("Aa"):
            print ('"It\'s correct congratulations."')
            time.sleep(2)
            print("You hear as you exit the room.")
            time.sleep(2)
            return True
        #Aqui ganas
        if answerToken in ("Cc"):
            print ('"Come on, you could\'ve done better than this."')
            time.sleep(2)
            print("You hear as you exit the room.")
            time.sleep(2)
            return False
        if answerToken in ("Dd"):
            print ("Really...")
            time.sleep(2)
            print("You hear as you exit the room.")
            time.sleep(2)
            return False
        return True

if __name__ == "__main__":
    tokenPuzzle()          
