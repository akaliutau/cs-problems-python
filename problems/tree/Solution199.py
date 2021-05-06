"""   Given a binary tree, imagine yourself standing on the right side of it,
   return the values of the nodes you can see ordered from top to bottom.
   
   Example:
   
   Input: [1,2,3,null,5,null,4] Output: [1, 3, 4] 
   Explanation:
   
           1        <--- bfs level 0
          / \ 
         2   3      <--- bfs level 1
          \   \ 
           5   4    <--- bfs level 2
   
   IDEA:
    1) use BFS traversing type for tree (i.e. by layers)
    2) in this type of traversal the last element in layer obviously will be the rightmost 
   
"""

class Solution199:
    pass
