"""   Given a binary tree, you need to compute the length of the diameter of the
   tree. The diameter of a binary tree is the length of the longest path between
   any two nodes in a tree. This path may or may not pass through the root.
   
     Example: 
     Given a binary tree 
                  1 
                 / \ 
                2   3
               / \ 
              4   5 
              
   Return 3, which is the length
   of the path [4,2,1,3] or [5,2,1,3].
   
   IDEA:
   use 2 answers:
   1) global var ans - for horizontal case which could or couldn't include root
   2) incremental path from cur node to the leaf - the return output for dfs
   
"""

class Solution543:
    pass