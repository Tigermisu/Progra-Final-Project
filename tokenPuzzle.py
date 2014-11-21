"""
Mini puzzle - Homeroid
5 tokens on my hand
"""
x = 0
def tokenPuzzle():
    print("A stranger ask you if you want to play a game")
    play = input('''"So what do you say?"\nA: Say me the game\nB: Nah\n''')
    while play not in ("A", "B", "a", "b"):
        play = input("Invalid command. Please choose again... \n")
    if play in ("B, b"):
        print('''"Come on, I know you want to"''')
        return x 
    else:
        print ("Okey let's play")
        print ('''"Let's see I have X tokens in my hand the there is five types of tokens \n Red(R), Black(B), Yellow(Y), White(W) and Green(G)"''')
        print ("If all my tokens are R execpt six,\n if all my tokens are G expect five\n I have all tokens W expect five and the rest are B and Y \n")
        print ("Note, each token only have one color")
        answerToken = input ('''"How many tokens do I have in my hand and how is the combination"\nA: R G G W W B Y(7) \nB: R R G B W Y(6) \nC: R G G W B Y Y (7) \nD: R G W B Y(5)\n ''')
        while answerToken not in ("A", "B", "a", "b","c","C","d","D"):
            answerToken = input("Invalid command. Please choose again... \n")
            if answerToken == ("B", "b"):
                print("NO")
                return  
            if answerToken == ("A, a"):
                print ("It's correct congratulations")
                return 
            if answerToken == ("C, c"):
                print ("Come you can do better than this")
                return  
            if answerToken == ("D, d"):
                print ("Really...")
                return
        return True
tokenPuzzle()          
