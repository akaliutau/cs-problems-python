"""   Given the head of a singly linked list where elements are sorted in ascending
   order, convert it to a height balanced BST.
   
   For this problem, a height-balanced binary tree is defined as a binary tree
   in which the depth of the two subtrees of every node never differ by more
   than 1.
   
   Input: head = [-10,-3,0,5,9] Output: [0,-3,9,-10,null,5] Explanation: One
   possible answer is [0,-3,9,-10,null,5], which represents the shown height
   balanced BST.
   
   IDEA:
   [1, 4, 7, 9]
   
   1) Recursively divide list and put left part to the left subbranch, and right part to the right subbranch
   
     [left, mid-1] [mid] [mid+1, right]
   
          [1, 4,   7,       9]
           |  |             |
           0  central       3
           mid == central elem
                  7
              /     \
         [1]         [7, 9]
         /               \ 
        1                 [2, 1][2][3,3]
                            \
                             2
                              \
                               3
                               
"""

class Solution109:
    pass
