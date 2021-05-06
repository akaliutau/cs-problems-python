"""   Given a string s, partition s such that every substring of the partition is a
   palindrome. Return all possible palindrome partitioning of s. 
   
   Example: Input:
   "aab" Output: [ ["aa","b"], ["a","a","b"] ]
   
   IDEA: 
   1) start with smallest cut, then expanding initial string
   2) apply this process recursively to the rest part of the string
   
   Example:
   aba = 
      a -> ba = a -> b - >a (when the index is out of boundary, add the tuple (a, b, a)) note, the strings structure will be updated for 3 cuts, specifically for parts aadded
      ab - dropped, because a!=b
      aba - added as a whole string, using info about internal part (string "b")
      
   
   
   
"""

class Solution131:
    pass
