"""   Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
   add spaces in s to construct a sentence where each word is a valid dictionary word. 
   Return all such possible sentences.
   
   
   Input: s = "catsanddog" wordDict = ["cat", "cats", "and", "sand", "dog"]
   Output: [ "cats and dog", "cat sand dog" ] 
   
   catsanddog
      |   |
    start end = 7  
   dp flow:
   
   dp: [
   idx list
   0   [""],
   1   [],
   2   [],
   3   ["cat"],
   4   ["cats"],
   5   [],
   6   [],
   7   ["cat sand","cats and"],
   8   [],
   9   [],
   10  []
   ]
   
   
"""

class Solution140:
    pass
