"""   Given an m x n matrix of non-negative integers representing the height of
   each unit cell in a continent, the "Pacific ocean" touches the left and top
   edges of the matrix and the "Atlantic ocean" touches the right and bottom
   edges.
   
   Water can only flow in four directions (up, down, left, or right) from a cell
   to another one with height equal or lower.
   
   Find the list of grid coordinates where water can flow to both the Pacific
   and Atlantic ocean.
   
   Example:
   
   Given the following 5x5 matrix:
   
   Pacific    ~  ~  ~  ~  ~ 
           ~  1  2  2  3 (5) * 
           ~  3  2  3 (4)(4) * 
           ~  2  4 (5) 3  1  * 
           ~ (6)(7) 1  4  5  * 
           ~ (5) 1  1  2  4  * 
              *  *  *  *  *  Atlantic
   
   Return:
   
   [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
   parentheses in above matrix)
   
   IDEA: 
   find the points which are peaks and meeting points in the same time 
   use marker +1 for one area and marker +2 for another one; the meeting point will have 1+2 == 3
"""

class Solution417:
    pass
