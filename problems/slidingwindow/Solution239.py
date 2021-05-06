"""   You are given an array of integers nums, there is a sliding window of size k 
   which is moving from the very left of the array to the very right. 
   You can only see the k numbers in the window. 
   Each time the sliding window moves right by one position.
   
   Window position              Max 
   ---------------             ----- 
   [1  3  -1] -3  5  3  6  7     3 
    1 [3  -1  -3] 5  3  6  7     3 
    1  3 [-1  -3  5] 3  6  7     5 
    1  3  -1 [-3  5  3] 6  7     5 
    1  3  -1  -3 [5  3  6] 7     6 
    1  3  -1  -3  5 [3  6  7]    7
    
    |      |   |     |  |  |
      blk1       blk2   blk3
      
    1  3  3| -3  5  5|  6  7     :: left  
    3  3 -1|  5  5  3|  7  7     :: right
    
    IDEA: 
    split on k-blocks and use partial sums to speed up 
"""

class Solution239:
    pass
