"""   Given a binary tree, return the sum of values of nodes with even-valued
   grandparent. (A grandparent of a node is the parent of its parent, if it
   exists.) 
   If there are no nodes with an even-valued grandparent, return 0
   
   IDEA:
   traverse the tree using a simulation:
   wrap each "traversed" node into Pair and preserve even-odd information within it
   
   0                  4            <--  has no parent so even=false
                    /   \
   1              3       8        <--  has an even parent "4"
                 /  \
   2           1     6             <--  has an odd parent "3"
                      \
   3                   2           <--  has an even parent "6"
   
   4
   
"""

class Solution1315:
    pass
