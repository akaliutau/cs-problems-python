"""   
   BFS
   
   You want to build a house on an empty land which reaches all buildings in the
   shortest amount of distance. You can only move up, down, left and right. You
   are given a 2D grid of values 0, 1 or 2, where:
   
   Each 0 marks an empty land which you can pass by freely. 
   
   Each 1 marks a building which you cannot pass through. 
   
   Each 2 marks an obstacle which you cannot pass through. 
   
   Example:
   
   Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]], OR
   
      1 - 0 - 2 - 0 - 1 
      |   |   |   |   | 
      0 - 0 - 0 - 0 - 0 
      |   |   |   |   | 
      0 - 0 - 1 - 0 - 0
   
   Output: 7
   
   Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at
   (0,2), the point (1,2) is an ideal empty land to build a house, as the total
   travel distance of 3+3+1=7 is minimal. So return 7.
   
   IDEA:
   1) perform BFS from each building and save the maps with [accumulated] distances to accDistToBuildings
   2) go through all empty cells and analyze only those of them which are reachable from all buildings (use map reachableBuildingsCount)
   
   
"""

class Solution317:
    pass
