"""
Mini puzzle - Homeroid
5 tokens on my hand
"""
import time

def tokenPuzzle():
    x = 0
    print("A voice asks you if you want to play a game.\n")
    play = input('''"So what do you say?"\nA: Say me the game\nB: Nah\n''')
    while play not in ("A", "B", "a", "b"):
        play = input("Invalid command. Please choose again... \n")
    if play in ("B, b"):
        print('''Wrong answer, pal''')
        time.sleep(2)
        tokenPuzzle()
    #Aqui empieza
    else:
        print ("Okay let's play")
        print ('''"Let's see I have X tokens in my hand the there is five types of tokens \n Red(R), Black(B), Yellow(Y), White(W) and Green(G)"''')
        print ("If all my tokens are R execpt six,\n if all my tokens are G expect five\n I have all tokens W expect five and the rest are B and Y \n")
        print ("Note, each token only has one color")
        answerToken = input('''"How many tokens do I have in my hand and how is the combination"\nA: R G G W W B Y(7) \nB: R R G B W Y(6) \nC: R G G W B Y Y (7) \nD: R G W B Y(5)\n ''')
        while answerToken.lower() not in ("abcd"):
            answerToken = input("Invalid command. Please choose again... \n")
        if answerToken in ("Bb"):
            print("NO.")
            return False
        if answerToken in ("Aa"):
            print ("It's correct congratulations.")
            return True
        #Aqui ganas
        if answerToken in ("Cc"):
            print ("Come on, you can do better than this.")
            return False
        if answerToken in ("Dd"):
            print ("Really...")
            return False
        return True

if __name__ == "__main__":
    tokenPuzzle()          
