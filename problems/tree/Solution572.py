"""   
   Given two non-empty binary trees s and t, check whether tree t has exactly
   the same structure and node values with a subtree of s. A subtree of s is a
   tree consists of a node in s and all of this node's descendants. The tree s
   could also be considered as a subtree of itself.
   
   
   2 Nodes are equal if: 
   
   1) they both empty 
   
   2) both have the same value 
   
   3) the same is true for each underlying level
   
   IDEA: consider each node in s as node and check subtrees on equality
   
   There are 2 dfs processes:
   1) dfs - needed to init the 2nd dfs with root @ the same level || asymmetric
   2) equals - actual check on tree's equality
   
   complexity: in worst case O(n^2)
"""

class Solution572:
    pass
