"""   
   Sliding window
   
   Given a string S, return the number of substrings of length K with no
   repeated characters.
   
   
   
   Example 1:
   
   Input: S = "havefunonleetcode", K = 5 Output: 6 Explanation: There are 6
   substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
   
   
   counter havefunonleetcode
   
   IDEA:
   1) for each letter in the string setup a counter and
   2) update unique counter each time when counter[let] hits 0, 1 or 2 (magic numbers)
   
   aaabac
      |||
      123
   
   0) a:3 unique=0
   
   1) a:2 b:1 unique=1
   
   2) a:2 b:1 unique=1
   
   3) a:2 b:1 c:1 unique=1+2=3
   
   
"""

class Solution1100:
    pass
