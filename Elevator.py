'''
este usa la lib time
'''
import time
def daElevaturr ():
    print('''\nStuck to the elevator's doors you find a note:\n\n"You may only go to where we allow you to, but we don't let just anyone in.\nFind "their" partners and you may proceed."\n''')
    time.sleep(5)
    print('''Inside the elevator you find yet another note on the number's panel,\nit shows a 4, a 6 and a 9...\nMaybe they're the floors you can access?\n''')
    time.sleep(5)
    print('''You press each button but nothing seems to happen....\nYou take a look at the note again and notice that on the backside\nthere is a number sequence:\n1:3, 2:3, 3:5, 4:?, 5:4, 6:?, 7:5, 8:5, 9:?, 10:3\n''')
    time.sleep(5)
    print('''And in very small font, you manage to work out another sentence:\n"The size of 1 is THREE, the size of TWO is 3 as well, what makes 3 be FIVE?"\n....Oh well.\n''')
    time.sleep(5)
    print('''Hmm... there seems to be small slots near the missing spaces,\nlet's try completing the sequence [0-9].''')
    time.sleep(4)
    answer = ["4", "3", "4"]
    panel = ["0", "0", "0"]
    querys = ["4", "6", "9"]
    

    while panel != answer:
        print("\n4:%s, 6:%s, 9:%s" % (panel[0], panel[1], panel[2]))
        for x in range (0,3):
            deci = (input('''What should we place with the %s?\n(Type "help" to get a hint and "seq" to check the sequence again)\n''' % (querys[x]))).lower()
            while deci not in ("0","1","2","3","4","5","6","7","8","9", "help", "seq"):
                deci = (input("Invalid command. Please choose again... \n")).lower()
            if deci == "help":
                print("Notice how the numbers on the second note are in capital letters?\nThere must be a connection between the numbers and those words")
                panel = ["0", "0", "0"]
                break
            elif deci =="seq":
                print("1:3, 2:3, 3:5, 4:?, 5:4, 6:?, 7:5, 8:5, 9:?, 10:3")
                break
            panel[x] = deci
            print("\n4:%s, 6:%s, 9:%s" % (panel[0], panel[1], panel[2]))
        else:
            if answer == panel:
                #Gano
                print('''You hear a high ping and the three buttons light up,\nlooks like you just restored the power!\n''')
                time.sleep(5)
                return
            else:
                #Incorrect
                panel = ["0", "0", "0"]
                print('''The panel makes a loud deep buzz and the slots reset....\nNot much changed...Well, keep at it!\n''')
                time.sleep(4)
                
if __name__ == '__main__':
    daElevaturr()
