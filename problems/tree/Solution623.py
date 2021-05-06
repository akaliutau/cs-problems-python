"""   Given the root of a binary tree, then value v and depth d, you need to add a
   row of nodes with value v at the given depth d. The root node is at depth 1.
   
   The adding rule is: given a positive integer depth d, for each NOT null tree
   nodes N in depth d-1, create two tree nodes with value v as N's left subtree
   root and right subtree root. And N's original left subtree should be the left
   subtree of the new left subtree root, its original right subtree should be
   the right subtree of the new right subtree root. If depth d is 1 that means
   there is no depth d-1 at all, then create a tree node with value v as the new
   root of the whole original tree, and the original tree is the new root's left
   subtree.
   
   
   Example 1: Input:
   
   A binary tree as following:   
       4 
      / \ 
     2   6
    / \ / 
   3  1 5
   
   v = 1
   
   d = 2
   
   Output:   
   
   
         4 
        / \ 
       1   1
      /     \
     2       6
    / \     /
   3   1   5
   
   IDEA:
   1) traverse tree using preorder
   2) be sure to have on each level:
      A. ref to parent node
      B. level on which the logic should be executed
      C. current level dynamically counted starting from 1 (root level = 1)
   
"""

class Solution623:
    pass
