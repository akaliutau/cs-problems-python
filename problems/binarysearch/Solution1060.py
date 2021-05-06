"""   Given a sorted array A of unique numbers, find the K-th missing number
   starting from the leftmost number of the array. 
   
   Example 1: Input: A =
   [4,7,9,10], K = 1 Output: 5 Explanation: The first missing number is 5.
   
   IDEA:
   
   orig:
   [4,7,9,10]
   
   full:
   [4,5,6,7,8,9,10]
    |     |
    l     r
   
   n-1   0
   
   10  - 4 = 6
   
   [4,7,9,10]
    |   |  |
    l   m  r  
    
"""

class Solution1060:
    pass
