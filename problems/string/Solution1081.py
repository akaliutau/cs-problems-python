"""   
   Given a string s, remove duplicate letters so that every letter appears once and only once. 
   You must make sure your result is the smallest in lexicographical order among all possible results.
   
   Example 1:
  
   Input: s = "bcabc"
   Output: "abc"
   
   IDEA:
   use freq map, iterate through array from back, removing duplicates on the way
   
   aswddefghjsd
    | ||     ||
    |        |
             |
            will be added after frequency nullification
    
    
   a        taken=[a]        a is single, will never be touched again (while loop stops)
   as       taken=[a,s]      s has a frequency 2, will be added one time NOTE: if a had freq > 1, then astua: astu < stua
   asw      taken=[a,s,w]    w is single, will never be touched again (while loop stops)
   aswd     taken=[a,s,w,d]
   aswde    taken=[a,s,w,d,e]
    
   complexity O(2n)
   
"""

class Solution1081:
    pass
