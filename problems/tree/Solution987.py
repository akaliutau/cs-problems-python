"""   Given a binary tree, return the vertical order traversal of its nodes values.
   
   For each node at position (X, Y), its left and right children respectively
   will be at positions (X-1, Y-1) and (X+1, Y-1).
   
   Running a vertical line from X = -infinity to X = +infinity, whenever the
   vertical line touches some nodes, we report the values of the nodes in order
   from top to bottom (decreasing Y coordinates).
   
   If two nodes have the same position, then the value of the node that is
   reported first is the value that is smaller. (SPECIAL CONDITION)
   
   Return an list of non-empty reports in order of X coordinate. Every report
   will have a list of values of nodes.
   
   
   
   Input: [3,9,20,null,null,15,7] 
   Output: [[9],[3,15],[20],[7]] 
   
             3
            / \
           9   20
              /  \
             15   7
   
   Explanation:
   Without loss of generality, we can assume the root node is at position (0, 0): 
   Then, the node with value 9 occurs at position (-1, -1); 
   The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2); 
   The node with value 20 occurs at position (1, -1); 
   The node with value 7 occurs at position (2, -2).
   
   IDEA:
   quite straightforward:
   1) DFS through tree, be aware of current level and column
   2) collect in map column => list of Pair(rows,value)
   3) update stat for min, max columns
   
   on the 2nd stage exract and sort all data from map
"""

class Solution987:
    pass
