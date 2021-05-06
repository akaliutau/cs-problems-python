"""   
   Given n pairs of parentheses, write a function to generate all combinations
   of well-formed parentheses.
   
   
   
   Example 1:
   
   Input: n = 3 Output: ["((()))","(()())","(())()","()(())","()()()"]
   
   IDEA:
   
   1) left branch - add ( until count < 3
   
   2) right branch - does not start until left branch exit
   
   
   			   ""
              /   \
             (     )
            / 
           (
          / \
         (   )
          \  | \
           ) (  )
            \
             )
              \
               )
         
"""

class Solution22:
    pass
