''' Riddles Puzzle'''

def riddles():
    print('''"As you approach to a black gate suddenly a strange man appears in front of you"\n-Well well well Mr. Jones, we meet again; I hope you are ready for what's next. You answer my riddles and you can continue with your adventure, you answer my riddles and you don't die. So, shall we begin?''')
    start= input("Are you ready?\nA: I'm ready\nB: NO\n")
    while start not in ("A", "B", "a", "b"):
        start = input("Invalid command. Please choose again... \n")
    if start in ("B, b"):
        print("Then prepare to meet your maker, farewell Mr. Jones")
    else:
        print("Then let's get started")
        riddle1= input("Riddle #1:\nWhat do you throw away that keeps returning?\nA: a girlfriend\nB: a balloon\nC: a boomerang\nD: food\n")
        while riddle1 not in ("A", "B", "C", "D", "a", "b", "c", "d"):
            riddle1=input("Invalid command. Please choose again... \n")
        if riddle1 in ("A", "B", "D", "a", "b", "d"):
            print("Nope, bye bye Mr. Jones")
        else:
            print("You are.... RIGHT!, Round 2")
            riddle2= input("Riddle #2:\How many sides has a circle?\nA: One\nB: Two\nC: None\nD: Infinite\n")
            while riddle2 not in ("A", "B", "C", "D", "a", "b", "c", "d"):
                riddle2= input("Invalid command. Please choose again... \n")
            if riddle2 in ("A", "C", "D", "a", "c", "d"):
                print("Once again, you've been defeated Mr. Jones")
            else:
                print("Congratulations, one step away from death, shall we continue?")
                riddle3= input("Riddle #3:\nWhat belongs to you, but is used by others?\nA: Your name\nB: Your Dignity\nC: Your House\nD: Your dog\n")
                while riddle3 not in ("A", "B", "C", "D", "a", "b", "c", "d"):
                    riddle3= input("Invalid command. Please choose again... \n")
                if riddle3 in ("B", "C", "D", "b", "c", "d"):
                    print("I guess you really want to die, farewell Mr. Jones")
                else:
                    print("Mmmm, seems like I've underestimated you. Now the last Riddle, fail me and your family dies, succeed and you may save them")
                    riddle4= input("Last Riddle:\nWhat is the beginning of eternity, the end of time and space, the beginning of every end and the end of every race?\nA: Life\nB: God\nC: Love\nD: Letter E\n")
                    while riddle4 not in("A", "B", "C", "D", "a", "b", "c", "d"):
                        riddle4= input("Invalid command. Please choose again... \n")
                    if riddle4 in ("A", "B", "C", "a", "b", "c"):
                        print("Well, seems like you don't care about dying, see you in hell")
                    else:
                        print("Mmmm, seems like this is our last goodbye... for now. You can go and pass the black gate and see what it has prepared for you. Farewell Mr. Jones, and good luck...")
