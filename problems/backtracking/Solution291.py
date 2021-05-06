"""   Given a pattern and a string s, return true if s matches the pattern. A
   string s matches a pattern if there is some bijective mapping of single
   characters to strings such that if each character in pattern is replaced by
   the string it maps to, then the resulting string is s. A bijective mapping
   means that no two characters mapping to the same string, and no character maps to
   two different strings. 
   
   Example 1: Input: pattern = "abab", s =
   "redblueredblue" Output: true 
   
   Explanation: One possible mapping is as
   follows: 'a' -> "red" 'b' -> "blue"
   
   IDEA: 
   1) start with smallest cut, then expanding initial string
   2) apply this process recursively to the rest part of the string
   
   Example:
   pattern = aba, s = bluewhiteblue
   
    
   
"""

class Solution291:
    pass
