"""   Given an input string (s) and a pattern (p), implement regular expression
   matching with support for '.' and '*' 
   where: '.' Matches any single character.​​​​ 
          '*' Matches zero or more of the preceding element. 
   
   The matching should cover the entire input string (not partial). 
   
   Example 1:
   Input: s = "aa", p = "a" Output: false Explanation: "a" does not match the
   entire string "aa"
   
   IDEA:
   1) start search from the tail
   2) subproblem
      remove the last symbol @pattern for pattern and compare against block 
      
    
       ""  a 
    "" 1   0 
    a  0   X
    a  0   1
    
   
"""

class Solution10:
    pass
