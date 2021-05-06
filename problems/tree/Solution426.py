"""   Convert a Binary Search Tree to a sorted Circular Double-Linked List in
   place. 
   
   You can think of the left and right pointers as synonymous to the
   predecessor and successor pointers in a double-linked list. For a circular
   double-linked list, the predecessor of the first element is the last element,
   and the successor of the last element is the first element. We want to do the
   transformation in place. After the transformation, the left pointer of the
   tree node should point to its predecessor, and the right pointer should point
   to its successor. You should return the pointer to the smallest element of
   the linked list. 
   
   IDEA:
   
   1) if to use INORDER traversing, the business logic will be executed one nodes as they are linked in list
   2) use global tuple (first, last) to form a chain segment
    
   Initiate the first and the last nodes as nulls. 
     Call the inorder recursion dfs(root) : 
      If node is not null : Call the recursion for the left subtree dfs(node.left). 
      If the last node is not null, link the last and the current node nodes. 
      Else initiate the first node. 
      Mark the current node as the last one : last = node.
      Call the recursion for the right subtree dfs(node.right). 
   Link the first and the last nodes to close DLL ring and then return the first node.
   
"""

class Solution426:
    pass
