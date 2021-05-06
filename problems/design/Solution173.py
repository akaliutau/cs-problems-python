"""   Implement an iterator over a binary search tree (BST). Your iterator will be
   initialized with the root node of a BST.
   
   Calling next() will return the next smallest number in the BST.
   
   
   
   Example:
             9
           /  \
          7    15
         / \     \
        3   8     20
        
   BSTIterator iterator = new BSTIterator(root); 
   iterator.next(); // return 3
   iterator.next(); // return 7 
   iterator.hasNext(); // return true
   iterator.next(); // return 9 
   iterator.hasNext(); // return true
   iterator.next(); // return 15 
   iterator.hasNext(); // return true
   iterator.next(); // return 20 
   iterator.hasNext(); // return false
   
   IDEA:
   1) collect on the stack the list of all leftmost nodes
   2) alg for each node:
      a) return the cur elem on the stack (which is always the leftmost)
      b) check the right branch - if exists, invoke leftmostInorder()
   
"""

class Solution173:
    pass
