''' Riddles Puzzle'''
'''Abraham Pineda'''
import time

def riddles():
    x=0
    riddle = 1
    print('''"As you approach to a black gate suddenly a strange man appears in front of you"\n-Well well well Mr. Jones, we meet again; I hope you are ready for what's next. You answer my riddles and you can continue with your adventure, you answer my riddles and you don't die. So, shall we begin?''')
    time.sleep(7)
    start= input("Are you ready?\nA: I'm ready\nB: NO\n")
    while start not in ("A", "B", "a", "b"):
        start = input("Invalid command. Please choose again... \n")
    if start in ("B","b"):
        print("Well, se you next time")
        return 3
    else:
        print("I'm afraid you don't have a choice, so let's get started!")
        time.sleep(3)
        print("Riddle #1:\nWhat do you throw away that keeps returning?")
        time.sleep(4)
        riddle1= input("A: a girlfriend\nB: a balloon\nC: a boomerang\nD: food\n")
        while riddle == 1:
            while riddle1 not in ("A", "B", "C", "D", "a", "b", "c", "d","exit"):
                riddle1=input("Invalid command. Please choose again... \n")
            if riddle1 == "exit":
                return 3
            if riddle1 in ("A", "B", "D", "a", "b", "d"):
                riddle = 2
            #pierde un punto
            if riddle1 in ("C","c"):
                x+=1 #gana un punto
                riddle = 2
        while riddle == 2:
            print("Riddle #2:\How many sides has a circle?")
            time.sleep(4)
            riddle2= input("A: One\nB: Two\nC: None\nD: Infinite\n")
            while riddle2 not in ("A", "B", "C", "D", "a", "b", "c", "d"):
                riddle2= input("Invalid command. Please choose again... \n")
            if riddle2 == "exit":
                return 3
            if riddle2 in ("A", "C", "D", "a", "c", "d"):
                #pierde un punto
                riddle = 3
            if riddle2 in ("b","B"):
                x+=1 #gana un punto
                riddle = 3
        while riddle == 3:
            print("Riddle #3:\nWhat belongs to you, but is used by others?")
            time.sleep(4)
            riddle3= input("\nA: Your name\nB: Your Dignity\nC: Your House\nD: Your dog\n")
            while riddle3 not in ("A", "B", "C", "D", "a", "b", "c", "d"):
                riddle3 = input("Invalid command. Please choose again... \n")
            if riddle3 == "exit":
                return 3
            if riddle3 in ("B", "C", "D", "b", "c", "d"):
                riddle = 4
                    #pierde punto
            if riddle3 in ("a", "A"):
                x+=1
                riddle = 4
        while riddle == 4:
            print("Last Riddle:\nWhat is the beginning of eternity, the end of time and space, the beginning of every end and the end of every race?")
            time.sleep(5)
            riddle4= input("A: Life\nB: God\nC: Love\nD: Letter E\n")
            while riddle4 not in("A", "B", "C", "D", "a", "b", "c", "d"):
                riddle4= input("Invalid command. Please choose again... \n")
            if riddle4 == "exit":
                return 3
            if riddle4 in ("A", "B", "C", "a", "b", "c"):
                riddle = 5#pierde punto
            if riddle4 in ("d", "D"):
                x+=1 #gana  punto
                riddle = 5
        if riddle == 5:
            if (x>=2):
                return True
                #GANASTE
            else:
                return False
                #Perdiste
                
if __name__ == "__main__":
    riddles()
