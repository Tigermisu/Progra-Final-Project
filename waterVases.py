import time

def printboard(sizes):
    print("\n     |A |  |B|  |C|\n\n     |%s%s|  |%s|  |%s|\n     --------------\nMAX: |10|  |7|  |3|" % (sizes[0],sizes[3],sizes[1],sizes[2]))

def waterVases():
    sizes = [10,0,0,""]
    maxs = [10,7,3]
    pos = {"a":0,"b":1,"c":2}
    print("As the door behind you closes, you hear water rushing.")
    time.sleep(3)
    print("Surprisingly there are fountains all over a place.")
    time.sleep(3)
    print("It looks as taken out of an Ancient Greece documental.")
    time.sleep(3)
    print("Unsurprisingly there appears to be another challenge for you.\n")
    time.sleep(3)
    print('"From these three vases you must retreat 5 liters of this special water.')
    time.sleep(3)
    print("Only the first one has water, but it holds 10 liters.")
    time.sleep(3)
    print("The empty vases can hold up to 7 and 3 liters each.")
    time.sleep(3)
    print('So you must use all three vases to achieve this goal."')
    time.sleep(3)
    print("\nAB means water on A into vase B, BC water on B into vase C.\nHowever once the water fills a vase, the remaining water stays on the original.\n")
    time.sleep(5)
    printboard(sizes)
    vase = ""
    while True and vase != "exit":
        vase = input('Which vases do you want to pour? [AB, "R" or "Exit"] ').lower()
        while vase not in ("ab","ac","ba","bc","ca","cb","r","exit"):
            vase = input("Invalid input, please try again... ").lower()
        if vase == "r":
            sizes = [10,0,0,""]
            print("You pour everything back to the first vase.")
            printboard(sizes)
        elif vase == "exit":
            pass
        else:
            sizes[pos[vase[1]]] += sizes[pos[vase[0]]]
            sizes[pos[vase[0]]] = 0
            if sizes[pos[vase[1]]] > maxs[pos[vase[1]]]:
                 sizes[pos[vase[0]]] = (sizes[pos[vase[1]]] - maxs[pos[vase[1]]])
                 sizes[pos[vase[1]]] = maxs[pos[vase[1]]]
            if sizes[0] < 10:
                sizes[3] = " "
            else:
                sizes[3] = ""
            printboard(sizes)
        if (sizes[0] == 5) or (sizes[1] == 5):
            break
    ########### PUZZLE CLEARED ############
    if vase == "exit":
        return 3
    else:
        print("Upon completing the task, the door unlocks, enabling you to go back.")
        time.sleep(3)
        return True
    ####WHAT IF PUZZLE IS CLEARED

if __name__ == "__main__":
    waterVases()
