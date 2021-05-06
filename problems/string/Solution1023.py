"""   A query word matches a given pattern if we can insert lowercase letters to
   the pattern word so that it equals the query. (We may insert each character
   at any position, and may insert 0 characters.)
   
   Given a list of queries, and a pattern, return an answer list of booleans,
   where answer[i] is true if and only if queries[i] matches the pattern.
   
   
   
   Example 1:
   
   Input: queries =
   ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
   "FB" Output: [true,false,true,true,false] Explanation: "FooBar" can be
   generated like this "F" + "oo" + "B" + "ar". "FootBall" can be generated like
   this "F" + "oot" + "B" + "all". "FrameBuffer" can be generated like this "F"
   + "rame" + "B" + "uffer".
   
   IDEA:
   find all occurrences of symbols from pattern in string, letter by letter
   Note the additional checks for Uppercase letters on the tail and between
  
"""

class Solution1023:
    pass
