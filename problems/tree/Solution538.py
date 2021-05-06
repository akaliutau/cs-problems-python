"""   Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
   such that every key of the original BST is changed to the original key plus
   sum of all keys greater than the original key in BST. 
   
   As a reminder, a binary search tree is a tree that satisfies these constraints: 
   
   1) The left subtree of a node contains only nodes with keys less than the node's key. 
   
   2) The right subtree of a node contains only nodes with keys greater than the node's key.
   
   3) Both the left and right subtrees must also be binary search trees.
   
   IDEA:
   use inorder traversing, but in reverse variant:
   right node -> central -> left node
   
"""

class Solution538:
    pass
