"""   Remove the minimum number of invalid parentheses in order to make the input
   string valid. Return all possible results. Note: The input string may contain
   letters other than the parentheses ( and ). 
   
   Example 1: Input: "()())()"
   Output: ["()()()", "(())()"]
   
   IDEA:
   1) count left and right balance:
     f.e. for the leftView balance:
     a) increment counter if char == '(' 
      and decrement if char == ')' - 
      as a result all situations like ()) will be covered
      if we get balance < 0, remove problem symbol which is extra ')' and investigate this case through dfs
         
   
"""

class Solution301:
    pass
