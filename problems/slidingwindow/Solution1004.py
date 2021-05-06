"""   Sliding window 
   
   Given an array A of 0s and 1s, we may change up to K values
   from 0 to 1. Return the length of the longest (contiguous) subarray that
   contains only 1s. 
   
   Input: A =   [1,1,1,0,0,0,1,1,1,1,0], K = 2 
   Output: 6
   Explanation: [1,1,1,0,0,1,1,1,1,1,1]
   
   IDEA: 
   use [left,right] as contiguous block and dynamically count 0s
   Rules:
   1) if there is no lack of 0s, increase the right boundary, leave the left one untouched
   
   
   |
   1,1,1,0,0,0,1,1,1,1,0,0
             | k=-1, get run of 0s to change
   
           |
   1,1,1,0,0,0,1,1,1,1,0,0
             | k = 0, got rid of 1 zero, now can continue extend right boundary
   
           |
   1,1,1,0,0,0,1,1,1,1,0,0
                       | k=-1
   
             |
   1,1,1,0,0,0,1,1,1,1,0,0
                         |
   
   
"""

class Solution1004:
    pass
