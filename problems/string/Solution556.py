"""   Given a positive 32-bit integer n, you need to find the smallest 32-bit
   integer which has exactly the same digits existing in the integer n and is
   greater in value than n. If no such positive 32-bit integer exists, you need
   to return -1. 
   
   Example 1: Input: 12 Output: 21
   
   IDEA:
   1) find 2 numbers (not necessarily consequent) to form a swap pair from the end
   2) swap them
   3) reverse the tail after left + 1 (because according the def of left, all seq [left,end] is DECREASING, => reverse to get the SMALLEST)
   
   123  <-- find the first number in swap pair - must be a pattern [num_1][num_2], num_1 < num_2, let's mark it i
   132  <-- to form a swap pair we have to find the 2nd number - 1) the 1st from the end meeting the criteria: as smaller than i+1 [3] as possible 
   
   213
   231
   
   312
   321
   
    
   
   12 -> 21
   21 -> 12 - wrong
   
   12354
     | |
   
   
   1320
   |
   
   1320
     |
   
   1320
   | |
   
   2310 -> 2013 [3 > 1 > 0] - the biggest
   
   
   [d0][BIGGEST]
   [d1]
   
   d0 - > d1
"""

class Solution556:
    pass
