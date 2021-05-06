"""   You are a hiker preparing for an upcoming hike. You are given efforts, a 2D
   array of size rows x columns, where efforts[row][col] represents the effort
   of cell (row, col). You are situated in the top-left cell, (0, 0), and you
   hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e.,
   0-indexed). You can move up, down, left, or right, and you wish to find a
   route that requires the minimum effort. A route's effort is the maximum
   absolute difference in efforts between two consecutive cells of the route.
   Return the minimum effort required to travel from the top-left cell to the
   bottom-right cell. 
   
   Input: efforts = 
   [
   [1,2,2],
   [3,8,2],
   [5,3,5]
   ] 
   
   Output: 2
   Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2
   in consecutive cells. This is better than the route of [1,2,2,2,5], where the
   maximum absolute difference is 3.
   
   IDEA (similar to 1102):
   
    As a result all cells in queue will be prioritized by min effort on the top => optimal 
      [not necessary the shortest] path 
      
   explicit greedy approach - we are trying the effortless paths first   
"""

class Solution1631:
    pass
