"""
Mini puzzle - Kagynt
10 marbles, 5 rows of 4 marbles
"""

def marblePuzzle ():
    print('''You're walking down the path when a shady figure approaches you.\n"Hey there fellow traveler! Care for a little wager?\nYou can win what I've obtained through my journeys!\nThat is, if you can beat me....\nBe warned, once you're in the game, there's no backing out."''')
    play = input('''"So what do you say?"\nA: Let's play\nB: Nah\n''')
    while play not in ("A", "B", "a", "b"):
        play = input("Invalid command. Please choose again... \n")
    if play in ("B, b"):
        print('''"Sigh, you rookies are all so boring, get lost"''')
        return 3
    else:
        grid = "-------------------\n|a0| |a1| |a2| |a3|\n-------------------\n   |b0| |b1| |b2|\n-------------------\n|c0| |c1| |c2| |c3|\n-------------------\n   |d0| |d1| |d2|\n-------------------\n|e0| |e1| |e2| |e3|\n-------------------\n   |f0| |f1| |f2|\n-------------------\n|g0| |g1| |g2| |g3|\n-------------------"
        print('''"Now that's what I call traveler spirit!"\nYou follow the man towards a small table with tiny orifices in it and he takes out 12 perfectly round and shiny black marbles''')
        see = input('''"You see this board right here?"\n'''+grid+'''\nA: Yep\nB: What?\n''')
        while see not in ("A", "B", "a", "b"):
            see = input("Invalid command. Please choose again... \n")
        if see in ("B,b"):
            print('''"....try looking at it?, anyways, moving forward....."''')
        print('''"You can only place one marble in each slot\nand you have to make a total of 6 rows of exactly 4 marbles each with these 12 marbles I give you."''')
        exa = input('''"Would you like an example?"\nA: Please\nB: I'm good\n''')
        while exa not in ("A", "B", "a", "b"):
            exa = input("Invalid command. Please choose again... \n")
        if exa in ("A, a"):
            print('''"An example of one row im asking for (you need 6 of these) is:"\n-------------------\n|. | |. | |. | |. |\n-------------------\n   |b0| |b1| |b2|\n-------------------\n|c0| |c1| |c2| |c3|\n-------------------\n   |d0| |d1| |d2|\n-------------------\n|e0| |e1| |e2| |e3|\n-------------------\n   |f0| |f1| |f2|\n-------------------\n|g0| |g1| |g2| |g3|\n-------------------\n"or"\n-------------------\n|. | |a1| |a2| |a3|\n-------------------\n   |. | |b1| |b2|\n-------------------\n|c0| |. | |c2| |c3|\n-------------------\n   |d0| |. | |d2|\n-------------------\n|e0| |e1| |e2| |e3|\n-------------------\n   |f0| |f1| |f2|\n-------------------\n|g0| |g1| |g2| |g3|\n-------------------''')
            ready = input('''"I better hope you're ready because I'm getting anxious now"\nA: Ready!!\nB: I'm a slow learner\n''')
            while ready not in ("A", "B", "a", "b"):
                ready = input("Invalid command. Please choose again... \n")
            if ready in ("A", "a"):
                print('"Well? What are you waiting for?!! Give it a go!"')
            else:
                print('''".....I'll just asume you'll be a natural"''')
        else:
            print('''"Well, I hope you know what you're doing."''')
        print("To place a marble type the slot's letter and number then press Enter.\nIf you want to take out a marble simply type that marble's slot again.\nAlso, if you want to reset the board, type R then press Enter.\nGood luck!")
        sol1 = "-------------------\n|a0| |. | |. | |a3|\n-------------------\n   |b0| |. | |b2|\n-------------------\n|c0| |. | |. | |c3|\n-------------------\n   |. | |d1| |. |\n-------------------\n|e0| |. | |. | |e3|\n-------------------\n   |f0| |. | |f2|\n-------------------\n|g0| |. | |. | |g3|\n-------------------"
        com = {"a":0, "c":0, "e":0,"g":0,"abcd0":0, "abcd1":0, "abcd2":0, "abcd3":0, "bcde0":0, "bcde1":0,"bcde2":0, "bcde3":0, "cdef0":0, "cdef1":0, "cdef2":0, "cdef3":0, "defg0":0, "defg1":0, "defg2":0, "defg3":0}
        sol2 = "-------------------\n|a0| |a1| |a2| |a3|\n-------------------\n   |b0| |. | |b2|\n-------------------\n|. | |. | |. | |. |\n-------------------\n   |. | |d1| |. |\n-------------------\n|. | |. | |. | |. |\n-------------------\n   |f0| |. | |f2|\n-------------------\n|g0| |g1| |g2| |g3|\n-------------------"
        slots = {"a0":"a0", "a1":"a1", "a2":"a2","a3":"a3", "b0":"b0", "b1":"b1", "b2":"b2", "c0":"c0", "c1":"c1", "c2":"c2", "c3":"c3", "d0":"d0", "d1":"d1", "d2":"d2", "e0":"e0", "e1":"e1", "e2":"e2", "e3":"e3", "f0":"f0", "f1":"f1", "f2":"f2", "g0":"g0", "g1":"g1", "g2":"g2", "g3":"g3"}
        pos = {}
        for x in slots:
            pos[x]=grid.index(x)
        win = False
        move =""
        remains = 12
        lines = 0
        #INTRO IS OVER!!! HERE COMES THE REAL DOUGH!!!!
        while not win:
            lines = 0
            for x in com:
                lines += com[x]
            print("|||||You have made "+str(lines)+" lines with " +str(12-remains)+" marbles|||||")
            print(grid)
            move = str(input("Where would you like to move? | Press r to restart | Type exit to give up\n").lower())
            while move not in ('r', 'exit', 'b1', 'c1', 'f1', 'd0', 'a1', 'b0', 'e0', 'a3', 'e3', 'a0', 'f0', 'g1', 'g3', 'd2', 'c0', 'e1', 'f2', 'e2', 'g2', 'c2', 'a2', 'd1', 'g0', 'b2', 'c3'):
                move = str(input("Invalid command. Please choose again... \n").lower())
            if move == "r":
                grid = "-------------------\n|a0| |a1| |a2| |a3|\n-------------------\n   |b0| |b1| |b2|\n-------------------\n|c0| |c1| |c2| |c3|\n-------------------\n   |d0| |d1| |d2|\n-------------------\n|e0| |e1| |e2| |e3|\n-------------------\n   |f0| |f1| |f2|\n-------------------\n|g0| |g1| |g2| |g3|\n-------------------"
                slots = {"a0":"a0", "a1":"a1", "a2":"a2","a3":"a3", "b0":"b0", "b1":"b1", "b2":"b2", "c0":"c0", "c1":"c1", "c2":"c2", "c3":"c3", "d0":"d0", "d1":"d1", "d2":"d2", "e0":"e0", "e1":"e1", "e2":"e2", "e3":"e3", "f0":"f0", "f1":"f1", "f2":"f2", "g0":"g0", "g1":"g1", "g2":"g2", "g3":"g3"}
                remains = 12
            elif move == "exit":
                return 3
            else:
                if slots[move] == move:
                    if remains > 0:
                        slots[move] = ". "
                        remains -= 1
                        for x in slots:
                            grid = grid.replace(x, slots[x])
                    else:
                        print("You don't have any remaining marbles")
                else:
                    slots[move] = move
                    remains += 1
                    lgrid = list(grid)
                    lgrid[pos[move]] = move[0]
                    lgrid[pos[move]+1] = move[1]
                    grid = ""
                    for x in lgrid:
                        grid+=x
            if grid[pos["a0"]+1] == grid[pos["a1"]+1] and grid[pos["a2"]+1] == grid[pos["a3"]+1]:
                com["a"] = 1
            else:
                com["a"] = 0
            if grid[pos["c0"]+1] == grid[pos["c1"]+1] and grid[pos["c2"]+1] == grid[pos["c3"]+1]:
                com["c"] = 1
            else:
                com["c"] = 0
            if grid[pos["e0"]+1] == grid[pos["e1"]+1] and grid[pos["e2"]+1] == grid[pos["e3"]+1]:
                com["e"] = 1
            else:
                com["e"] = 0
            if grid[pos["g0"]+1] == grid[pos["g1"]+1] and grid[pos["g2"]+1] == grid[pos["g3"]+1]:
                com["g"] = 1
            else:
                com["g"] = 0
            if grid[pos["a0"]] == grid[pos["b0"]] and grid[pos["c1"]] == grid[pos["d1"]]:
                com["abcd0"] = 1
            else:
                com["abcd0"] = 0
            if grid[pos["a1"]] == grid[pos["b1"]] and grid[pos["c2"]] == grid[pos["d2"]]:
                com["abcd1"] = 1
            else:
                com["abcd1"] = 0
            if grid[pos["a2"]] == grid[pos["b1"]] and grid[pos["c1"]] == grid[pos["d0"]]:
                com["abcd2"] = 1
            else:
                com["abcd2"] = 0
            if grid[pos["a3"]] == grid[pos["b2"]] and grid[pos["c2"]] == grid[pos["d1"]]:
                com["abcd3"] = 1
            else:
                com["abcd3"] = 0
            if grid[pos["b0"]] == grid[pos["c1"]] and grid[pos["d1"]] == grid[pos["e2"]]:
                com["bcde0"] = 1
            else:
                com["bcde0"] = 0
            if grid[pos["b1"]] == grid[pos["c1"]] and grid[pos["d0"]] == grid[pos["e0"]]:
                com["bcde1"] = 1
            else:
                com["bcde1"] = 0
            if grid[pos["b1"]] == grid[pos["c2"]] and grid[pos["d2"]] == grid[pos["e3"]]:
                com["bcde2"] = 1
            else:
                com["bcde2"] = 0
            if grid[pos["b2"]] == grid[pos["c2"]] and grid[pos["d1"]] == grid[pos["e1"]]:
                com["bcde3"] = 1
            else:
                com["bcde3"] = 0
            if grid[pos["c0"]] == grid[pos["d0"]] and grid[pos["e1"]] == grid[pos["f1"]]:
                com["cdef0"] = 1
            else:
                com["cdef0"] = 0
            if grid[pos["c1"]] == grid[pos["d1"]] and grid[pos["e2"]] == grid[pos["f2"]]:
                com["cdef1"] = 1
            else:
                com["cdef1"] = 0
            if grid[pos["c2"]] == grid[pos["d1"]] and grid[pos["e1"]] == grid[pos["f0"]]:
                com["cdef2"] = 1
            else:
                com["cdef2"] = 0
            if grid[pos["c3"]] == grid[pos["d2"]] and grid[pos["e2"]] == grid[pos["f1"]]:
                com["cdef3"] = 1
            else:
                com["cdef3"] = 0
            if grid[pos["d0"]] == grid[pos["e1"]] and grid[pos["f1"]] == grid[pos["g2"]]:
                com["defg0"] = 1
            else:
                com["defg0"] = 0
            if grid[pos["d1"]] == grid[pos["e1"]] and grid[pos["f0"]] == grid[pos["g0"]]:
                com["defg1"] = 1
            else:
                com["defg1"] = 0
            if grid[pos["d1"]] == grid[pos["e2"]] and grid[pos["f2"]] == grid[pos["g3"]]:
                com["defg2"] = 1
            else:
                com["defg2"] = 0
            if grid[pos["d2"]] == grid[pos["e2"]] and grid[pos["f1"]] == grid[pos["g1"]]:
                com["defg3"] = 1
            else:
                com["defg3"] = 0
            if grid == sol1 or grid == sol2:
                win = True
        print(grid)
        print('"Damn it! You won."\n')
        return True

if __name__ == "__main__":
    marblePuzzle()
