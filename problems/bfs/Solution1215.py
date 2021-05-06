"""   A Stepping Number is an integer such that all of its adjacent digits have an
   absolute difference of exactly 1. For example, 321 is a Stepping Number while
   421 is not. Given two integers low and high, find and return a sorted list of
   all the Stepping Numbers in the range [low, high] inclusive. 
   Example 1:
   Input: low = 0, high = 21 Output: [0,1,2,3,4,5,6,7,8,9,10,12,21] 
   
   IDEA:
   
   BFS: start
   node = 0 From 0, we can move to 1 2 3 4 5 6 7 8 9 
   from 1 -> 12 and 10 
   from 2 -> 23 and 21 
   from 3 -> 34 and 32
"""

class Solution1215:
    pass
