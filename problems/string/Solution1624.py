"""   Given a string s, return the length of the longest substring between two
   equal characters, excluding the two characters. If there is no such substring
   return -1.
   
   A substring is a contiguous sequence of characters within a string.
   
   
   Example 1:
   
   Input: s = "aa" Output: 0 Explanation: The optimal substring here is an empty
   substring between the two 'a's. Example 2:
   
   Input: s = "abca" Output: 2 Explanation: The optimal substring here is "bc".
   
   IDEA:
   use the map for positions of letters map: letter => last_seen_index
   
   Note the edge case abbaccccca - index['a'] will be used for the s=1st occurrence of 'a'
   
"""

class Solution1624:
    pass
