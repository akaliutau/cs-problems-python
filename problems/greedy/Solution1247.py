"""   You are given two strings s1 and s2 of equal length consisting of letters "x"
   and "y" only. Your task is to make these two strings equal to each other. You
   can swap any two characters that belong to different strings, which means:
   swap s1[i] and s2[j]. Return the minimum number of swaps required to make s1
   and s2 equal, or return -1 if it is impossible to do so. 
   
   Example 1: Input: s1
   = "xx", s2 = "yy" Output: 1 
   
   Explanation: Swap s1[0] and s2[1], s1 = "yx", s2
   = "yx".
   
             M       M     M 
    s1 - X X Y Y X Y X Y X X 
         | | | | | | | | | | 
    s2 - X Y Y X Y X X X Y X
    
    
     S1 - S2 : (Mis-Matched)
   1. X - Y  :     3
   2. Y - X  :     3
   
   If total mismatched i.e, X-Y(MisMatched) + Y-X(MisMatched) == odd (Then return -1 no ans is possible)
"""

class Solution1247:
    pass
