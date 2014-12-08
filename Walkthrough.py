'''
THE SOLE PURPOSE OF THIS DOCUMENT IS TO SERVE AS A WALKTHROUGH FOR OUR GAME

Firstly, depending on how many puzzles you solve, is the difficulty of the last puzzle.
Namely, if you only solve one or two puzzles per area, you get the hardest puzzle at the end for being lazy.
And if you solve more than that (5-6 of 6), you will get the easiest final puzzle.

########################################
#############ELEVATOR PUZZLE############
########################################

The puzzle consisted on finding the answer to a sequence.
The answer is as follows:
4 = FOUR
6 = SIX
9 = NINE

So 4:4, 6:3, 9:3, the lenght of each word.

#################################
#############FLOOR #4############
#################################

Even though a redo option wouldn't have been difficult to implement, this puzzle was to be done on one try.
(This puzzle is from the IXth Century.)

You have to make the chess knight travel across the board, there are many solutions for this one.
Here is one solution:

1 > 1 > 1 > 5 > 2 > 1 > 2 > 3 > 2 > 2 > 2 > 1 > 3 > 1 > 2 >
1 > 2 > 2 > 1 > 1 > 2 > 1 > 1 > 3 > 2 > 1 > 1 > 1 > 1

Remember you can always try again if you wish to!

#################################
#############FLOOR #6############
#################################

You may only attempt to do this puzzle once, so think carefully.

This scale problem changes the solution everytime you play it.
There are nine weights, and you can use the scale only twice.
You must find the weight that is the heaviest.

The solution is quite simple, you first put three weights on each side.
If the scale moves to either side, it means the heaviest is on that side.
If it stays put, it means that the heaviest is among the three that weren't chosen.

As for the second round, you now know the heviest is between 3 weights.
Repeat the process by placing one weight on each side.
If it tilts to either side, it means that weight is the heaviest.
If it stays put, it means is the third one you didn't choose.

#################################
#############FLOOR #9############
#################################

For this puzzle you basically need to find a sequence.
You must press ABCD in the correct order

You can either try all the 16 possible combinations really quick.
Or you can pay attention how long it takes the music to go off after trying each option.

You will notice that:
After selecting B, it will keep delievering sound for 4 turns.
C will do so for 3.
A will last 2.
While D will turn off the next movement you make.

Therefore the answer is BCAD.

Failing to complete this puzzle leads to the game over sequence.

#################################
#########NUMBERLESS FLOOR########
#################################

This floor holds a somewhat hard math puzzle.
You need to find the sum of the multiples 3 and 5, below 1000.
To speed up the process you have in your power a moldule machine.
This machine will same up all the numbers of the modulo you chose.
And you can use the sum machine afterwards to sum these quantities automatically.
You also count with an old calculator.
We could've used eval() to have a normal calculator.
But we preferred not to to make the player think instead of summing all the numbers.

You may choose the path of your preference to solve this puzzle.

The answer is 233168, which you can input on the dials (Option A).

#################################
##########MEDIEVAL HALL##########
#################################

Unlinke the elevator, there is no puzzle here, you can choose any path you like.

#################################
###########MARBLE PATH###########
#################################

This was difficult to implement, as the normal board needed diagonals.
That is why of the irregular board.

The goal is to make 6 rows of 4 marbles aligned with 12 marbles.

The answer is simple: The david star or:
b1, c0, c1, c2, c3, d0, d2, e0, e1, e2, e3, f1

#################################
########WATER VASES LANE#########
#################################

This must be one of the easiest puzzles.
You are provided with 3 vases with a capacity of 10, 7 and 3 liters.
You must somehow make that any of these vases hold exactly 5 liters.
At the beggining only the 10 liter vase was water.

You can take your time, or pour the water like this for a direct answer:
AB BC CA BC CA BC AB BC 

#################################
##########TOKENS STROLL##########
#################################

This is a gift, in case the player did very bad on the past puzzles.
It is a logic puzzle, the answer is A.

#################################
##########MOVING STATUES#########
#################################

If you were a good boy and completed at least 4 of the 6 non-obligatory puzzles (When you could select rooms),
you end up with this special easy puzzle.
It may look tricky at first, but the answer is simple:

5 > 3 > 2 > 4 > 6 > 7 > 5 > 3 > 1 > 2 > 4 > 6 > 5 > 3 > 4

CONGRATULATIONS UPON BEATING THE GAME!

#################################
##########COLOR TORCHES##########
#################################

If you did less than 4 of the 6 non-obligatory puzzles, you end here.
This puzzle is extremely difficult.

When you slect a torch, the adjascent ones will change along it.
Alternating on a sequence of three colors as explained.

There is a direct answer though:
B2 > D3 > E5 > C4 > E4 > A3 > B4 > E1 > C1 > A1 > D2

It takes a while to understand the path you need to take to solve this one.
Once you finish though...

CONGRATULATIONS UPON BEATING THE GAME!
'''
