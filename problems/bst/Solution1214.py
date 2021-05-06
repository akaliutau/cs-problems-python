"""   Given two binary search trees, return True if and only if there is a node in
   the first tree and a node in the second tree whose values sum up to a given
   integer target 
   
   Input: root1 = [2,1,4], root2 = [1,0,3], target = 5 Output:
   true 
   
   Explanation: 2 and 3 sum up to 5.
   
   IDEA: the same as 2sum problem with sorted array with some corrections:
   1) create a set of complementary numbers - such that if (target - some_val_tree_1) = some_val_tree_2, => some_val_tree_1 + some_val_tree_2 = target
   
"""

class Solution1214:
    pass
