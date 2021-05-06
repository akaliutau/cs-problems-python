"""   
   Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
   is a pair of nodes), write a function to check whether these edges make up a
   valid tree.
   
   Example 1:
   
   Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]] Output: true
   
   IDEA
   
   
   For the graph to be a valid tree, it must have exactly n - 1 edges. 
   
   Any less, and it can't possibly be fully connected. 
   
   Any more, and it has to contain cycles. 
   
   Additionally, if the graph is fully connected and contains exactly n - 1 edges, 
   it can't possibly contain a cycle, and therefore must be a tree!
   
   1) check that n - 1 == edges.size
   2) start tree traversal using BFS from any node (use bi-directional traversing) - must visit all n nodes.
"""

class Solution261:
    pass
