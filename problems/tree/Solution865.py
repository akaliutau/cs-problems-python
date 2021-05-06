"""   Given the root of a binary tree, the depth of each node is the shortest
   distance to the root.
   
   Return the smallest subtree such that it contains all the deepest nodes in
   the original tree.
   
   A node is called the deepest if it has the largest depth possible among any
   node in the entire tree.
   
   The subtree of a node is tree consisting of that node, plus the set of all
   descendants of that node.
   
   IDEA:
   1) for each node traverse both left and right branches, then
   2) choose the deepest branch and return it as an answer
   
   Expected result: 1-way path without forks or 1-way path with fork on one end:
             3                      3 
            / \                    / \
           4   5                  5   3
          /                      / \
         4                      2   4
"""

class Solution865:
    pass
