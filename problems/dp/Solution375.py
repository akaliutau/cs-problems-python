"""   We are playing the Guessing Game. The game will work as follows: 
   I pick a number between 1 and n. You guess a number. 
   If you guess the right number, you win the game. 
   If you guess the wrong number, then I will tell you whether
   the number I picked is higher or lower, and you will continue guessing. 
   Every time you guess a wrong number x, you will pay x dollars. If you run out of
   money, you lose the game. 
   
   Given a particular n, return the minimum amount of
   money you need to guarantee a win regardless of what number I pick.
   
   IDEA:
   the game easily can be reduced to subgames with the same structure
   
   Base case:
   [low, high=low]
   return low as a cost
   
   1) find a global optimal solutions by rebuilding the whole tree of possibilities
   2) use cache to reduce complexity 
   
"""

class Solution375:
    pass
