"""   Given an integer matrix, find the length of the longest increasing path. From
   each cell, you can either move to four directions: left, right, up or down.
   You may NOT move diagonally or move outside of the boundary (i.e. wrap-around
   is not allowed). 
   
   Example 1: 
   nums = 
   [ 
   [9,9,4], 
   [6,6,8], 
   [2,1,1] 
   ]
   Output: 4 
   
   Explanation: The longest increasing path is [1, 2, 6, 9].
   
   IDEA: 
   build path from pieces
   1) for each cell (i,j): build the longest path starting at (i,j) and save it in memo
   2) regardless of found order for each piece, the final resulting longest path will be found
    proof: 
    if start at cell 1, will be found pieces 1 -> 8, or the actual result 1 -> 2 -> 6 -> 9
    if start at cell 6, will be found pieces 6 -> 8, 6 -> 9
   
"""

class Solution329:
    pass
