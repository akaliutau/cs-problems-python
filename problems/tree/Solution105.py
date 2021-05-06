"""   
   Given preorder and inorder traversal of a tree, construct the binary tree.
   
   Note: You may assume that duplicates do not exist in the tree.
   
   For example, given
   
   preorder = [3,9,20,15,7] inorder = [9,3,15,20,7] Return the following binary
   tree:
   
          3 
         / \
        9   20 
            / \ 
           15  7
           
     [9,3,15,20,7]
       0 1 2 3 4
           
    IDEA:
    1) use info about preorder to traverse tree
    2) use inorder info to terminate tree building
    3) use mapping nodeId/val => its linear center  
    
    Algorithm:
    1) traverse and build tree in preorder manner 
    2) us mapping of value to the its index in the in-order array - 
       if an array built  from indecies [left, right] has a 0 length, that exit building immediately 
    
"""

class Solution105:
    pass
