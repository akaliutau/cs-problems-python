"""   Given inorder and postorder traversal of a tree, construct the binary tree.
   Note: You may assume that duplicates do not exist in the tree. For example,
   given inorder = [9,3,15,20,7] postorder = [9,15,7,20,3] Return the following
   binary tree: 
   
        3 
      /    \ 
    9       20 
           /   \ 
          15    7
      
    0   1  2 3  4
             |
           index  
           
    IDEA (the same as in 105):
    1) use info about postorder to traverse tree
    2) use inorder info to terminate tree building
    3) use mapping nodeId/val => its linear center  
      
"""

class Solution106:
    pass
