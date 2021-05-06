"""   Find the length of the longest substring T of a given string (consists of
   lowercase letters only) such that every character in T appears no less than k
   times. 
   
   Example 1: Input: s = "aaabb", k = 3 Output: 3 The longest substring
   is "aaa", as 'a' is repeated 3 times. 
   
   
   IDEA: 
   
   1) The sliding window slides over the string s and validates each character. 
   
   Based on certain conditions, the sliding window either expands or shrinks, namely: 
   
         === A substring is valid if each character has at least k frequency === 
   
   find all valid substrings with a different number of distinct characters and track the maximum
   length
   
   O(nU)
"""

class Solution395:
    pass
