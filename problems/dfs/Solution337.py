"""   The thief has found himself a new place for his thievery again. There is only
   one entrance to this area, called the "root." Besides the root, each house
   has one and only one parent house. After a tour, the smart thief realized
   that "all houses in this place forms a binary tree". It will automatically
   contact the police if two directly-linked houses were broken into on the same
   night.
   
   Determine the maximum amount of money the thief can rob tonight without
   alerting the police.
   
   Algorithm
   
   Use a helper function which receives a node as input and returns a
   two-element array, where the first element represents the maximum amount of
   money the thief can rob if starting from this node without robbing this node,
   and the second element represents the maximum amount of money the thief can
   rob if starting from this node and robbing this node.
   
   The basic case of the helper function should be null node, and in this case,
   it returns two zeros.
   
   Finally, call the helper(root) in the main function, and return its maximum
   value.
   
   IDEA:
   construct a repeatable situation where there is a need to make a choice
   1) cost to rob this node and not robe neighbors
   2) cost not to rob this node, and investigate the cost of robbing neighbors in different combinations
   
"""

class Solution337:
    pass
