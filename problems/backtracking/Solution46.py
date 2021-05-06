"""   Given a collection of distinct integers, return all possible permutations.
   
   IDEA:
   for each iteration:
    1) choose the last number
    2) swap it with all the rest numbers, including the last one - as a result the last number iterates through all possible values
    3) Repeat until length=1 has reached 
   
               123          +1 new 
               
           32 1   13 2      +2 new after swaps 3-1, 3-2 and continue on [0,1]
          23 1    31  2     +2 new after swaps 2-3, 3-1 and continue on [0,0] // cycle ends here as len = 1
               12 3         +0 new 
               21 3         +1 new
   total = 6 = 3!            
"""

class Solution46:
    pass
