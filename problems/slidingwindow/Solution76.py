"""   
   Sliding window
   
   Given a string S and a string T, find the minimum window in S which will
   contain all the characters in T in complexity O(n).
   
   Example:
   
   Input: S = "ABAACBAB" T = "ABC" 
   Output: "ACB"
   
   IDEA:
   
   Flow:
   
   1) init state
   |
   ABAACBAB
   |
   
   2) the first desirable window
   |
   ABAACBAB
       |
   
   3) still desirable
    |
   ABAACBAB
       |
   
   4) no more desirable
     |
   ABAACBAB
       |
   
   5) desirable
     |
   ABAACBAB
        |
   
   6) answer (repeating will not improve this result)
      |
   ABAACBAB
        |
   
   
"""

class Solution76:
    pass
