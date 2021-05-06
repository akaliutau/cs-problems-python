"""   Given a matrix of integers grid with R rows and C columns, find the maximum
   score of a path starting at [0,0] and ending at [R-1,C-1].
   
   The score of a path is the minimum value in that path. For example, the value
   of the path 8 → 4 → 5 → 9 is 4.
   
   grid path moves some number of times from one visited cell to any neighbouring
   unvisited cell in one of the 4 cardinal directions (north, east, west,
   south).
   
   
   
   Example 1:
   
   Input: 
   [ 
   [5,4,5], 
   [1,2,6], 
   [7,4,6]
   ]
   
   Output: 4 (5 -> 4 -> 5 -> 6 -> 6)
   
   IDEA:
   1) the score of the whole path is determined by the min value in the chain 
      => the winning strategy will be to avoid min as long until it's possible
      
      Use  PriorityQueue to pick up next the cell with the max score FIRST, among all neighbors
      
      As a result all cells in queue will be prioritized with the max score on the top => optimal 
      [not necessary the shortest] path 
   
"""

class Solution1102:
    pass
