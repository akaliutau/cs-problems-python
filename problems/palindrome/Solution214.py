"""   Given a string s, you can convert it to a palindrome by adding characters in
   front of it. Find and return the shortest palindrome you can find by
   performing this transformation. 
   
   Example 1: Input: s = "aacecaaa" Output: "aaacecaaa" 
   
   
   IDEA: 
   
   s=abac
   
   the longest string is caba|abac
   which can be represented as 2 interlaced parts:
   
   caba      <-- reversed
       abac  <-- original
       
   final overlacing
       
   caba      <-- reversed
    abac     <-- original
       
   the answer should be c+abac
   
   Basically we have to find the longest interlaced substrings in str1 and str2
   Use Robin-Karp approach to calculate rolling hash
   
   original: rolling-hash sum for growing string [:i]  
   reversed: rolling-hash sum for growing string [n-i:n] - total length n - (n -i) = i
   
   
   rolling sum for original: 
     17^2 * a + 17 * b + a = 17^n * next_letter + prev_sum
     
   rolling sum for reversed: 
     17^2 * a + 17 * b + a = 17 * prev_sum + next_letter
   
   
"""

class Solution214:
    pass
