"""   Strings a and b are K-similar (for some non-negative integer K) if we can
   swap the positions of two letters in a exactly K times so that the resulting
   string equals b. Given two anagrams a and b, return the smallest K for which
   a and b are K-similar. 
   Example 1: Input: a = "ab", b = "ba" Output: 1 
   Example 2: Input: a = "abc", b = "bca" Output: 2
   
   IDEA:
   1) generate a space of all words-neighbors 
   2) perform a BFS on this space starting from word = a with target at b
   
"""

class Solution854:
    pass
