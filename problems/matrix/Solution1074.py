"""   
   Given a matrix and a target, return the number of non-empty submatrices that
   sum to target.
   
   A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x
   <= x2 and y1 <= y <= y2.
   
   Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if
   they have some coordinate that is different: for example, if x1 != x1'.
   
   
   
   Example 1:
   
   
   Input: matrix = 
   [ 
   [0,1,0], 
   [1,1,1], 
   [0,1,0] 
   ], target = 0 Output: 4
   
   Diagonal sum:
   [5,4,1], 
   [4,3,1], 
   [1,1,0]
   
   
   
   
   Explanation: The four 1x1 submatrices that only contain 0.
   
   IDEA:
   
   BF: one-time scan cost - O(n^2) Total time complexity O(n^4 X n^2) ~ O(n^6)
   
   Use pre-calculated 2D sums for each (i,j)
   preSum[j][i] == sum of all elements which are higher than row=i at column j
   (obviously for the 1st row all sums = 0)
   
   [0,1,0] -\    [0,0,0]
   [1,1,1]   \-  [0,1,0]
   [0,1,0]       [1,2,1]
                 [1,3,1]
                 
   check all sqs:
   
   #  ##  ###
   
   #  ##  ###
   #  ##  ###
   
   
   
"""

class Solution1074:
    pass
