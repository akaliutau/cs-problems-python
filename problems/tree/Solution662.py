"""   Given a binary tree, write a function to get the maximum width of the given
   tree. The maximum width of a tree is the maximum width among all levels. 
   
   The
   width of one level is defined as the length between the end-nodes (the
   leftmost and right most NON-NULL nodes in the level, 
   NOTE: the null nodes between the end-nodes are also counted into the length calculation. 
   
   It is
   guaranteed that the answer will in the range of 32-bit signed integer.
   
   
   Example 1:  Input: 
          1           <-- depth = 0, col = 0
         / \ 
        3   2         <-- depth = 1
       / \   \ 
      5   3   9       <-- depth = 2
      
      Output: 4 Explanation: The maximum
   width existing in the third level with the length 4 (5,3,null,9).
   
   Edge case:
   
          1           <-- depth = 0, col = 0
         / \ 
        3   2         <-- depth = 1
         \   \ 
          3   9       <-- depth = 2
         / \ / \
        4   67  9
        
    IDEA:
    1) use preorder traversing, the right branch first
    2) for each level hold a mapping recursion depth => index of first rightmost elem (collected naturally due to preorder)
"""

class Solution662:
    pass
