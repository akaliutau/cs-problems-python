"""   Given the root of a binary tree, return the sum of values of its deepest leaves.
   
   IDEA:
   Traverse all nodes (does not matter in which order)
   For each node must to have in local vars:
    1) current level of recursion
    2) result structure
    
    Process 2 cases for leaves:
    1) we have a better (== deeper) level - reset the result
    2) update the sum if the leaf is on the same level
"""

class Solution1302:
    pass
