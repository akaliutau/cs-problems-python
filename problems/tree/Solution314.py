"""   
   Given a binary tree, return the vertical order traversal of its nodes'
   values. (ie, from top to bottom, column by column).
   
   If two nodes are in the same row and column, the order should be from left to
   right.
   
   Examples 1:
   
   Input: [3,9,20,null,null,15,7]
   
         3 
        /  \ 
       9    20
           /  \ 
          15   7
         
      -1 0 1 2 3
   
   Output:
   
   [ 
    [9],    <-- each array represents the vertical slope
    [3,15], 
    [20], 
    [7]
   ]
   
   IDEA:
   Straightforward - 
   1) preorder traversing + be aware of index of current column
   
   2) collect in  map: col_index => list all the nodes from specific column
   
"""

class Solution314:
    pass
