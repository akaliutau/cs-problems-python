"""   Given a palindromic string palindrome, replace exactly one character by any
   lowercase English letter so that the string becomes the lexicographically
   smallest possible string that isn't a palindrome. After doing so, return the
   final string. If there is no way to do so, return the empty string. 
   
   Example 1: Input: palindrome = "abccba" Output: "aaccba" 
   
   Example 2: Input: palindrome
   = "a" Output: ""
   
   IDEA:
   find any non 'a' letter starting from index 0 and change it to 'a'
   
   after change: 
   1) string is not a palindrome anymore, because changes to diff letter 
   2) lexicographically smaller, because letter bigger than 'a' has been changed to a
"""

class Solution1328:
    pass
