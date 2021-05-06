"""   A group of two or more people wants to meet and minimize the total travel
   distance. You are given a 2D grid of values 0 or 1, where each 1 marks the
   home of someone in the group. The distance is calculated using Manhattan
   Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
   
   Example:
   
   Input:
   
            GRID                   HORIZONTAL DISTANCE
      1 - 0 - 0 - 0 - 1         *---|----------------*
      |   |   |   |   |             |
      0 - 0 - 0 - 0 - 0             | 
      |   |   |   |   |             |
      0 - 0 - 1 - 0 - 0             |-------* 
                                 any point 
                                 
                                    |<----->|   <---- overlapping range - to make it as small as possible, choose MEDIAN POINT as an optimum
   Output: 6
   
   Explanation: Given three people living at (0,0), (0,4), and (2,2): The point
   (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is
   minimal. So return 6.
   
   IDEA:
   
   SEE THE DIAGRAMM
   
   calculate the divergence between MEDIAN POINT (orig) and rows |row0 - orig| + |row1 - orig| + |row2 - orig| 
   
   rows = [0,0,2]
   cols = [0,2,4]
   
   1,8,10
   
   7   6
   2   3
   0   1 
   =9  =10
   
"""

class Solution296:
    pass
