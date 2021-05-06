"""   We can scramble a string s to get a string t using the following algorithm:
   
   If the length of the string is 1, stop. If the length of the string is > 1,
   do the following: Split the string into two non-empty substrings at a random
   index, i.e., if the string is s, divide it to x and y where s = x + y.
   Randomly decide to swap the two substrings or to keep them in the same order.
   i.e., after this step, s may become s = x + y or s = y + x. Apply step 1
   recursively on each of the two substrings x and y. Given two strings s1 and
   s2 of the same length, return true if s2 is a scrambled string of s1,
   otherwise, return false.
   
   
   
   Example 1:
   
   Input: s1 = "great", s2 = "rgeat" Output: true
   
   IDEA:
   generate all possible variants
   for speed up comparison of final parts use letter distribution calculations
   
    original         referenced
   -----------      ------------
   a_1 a_2 a_3      b_1 b_2 b_3
   
   on each iteration check 2 mapping variants:
   a_1|a_2 a_3      b_1 -> a_1 OR b_2 b_3 -> a_2 a_3
   
   a_1 a_2 | a_3    b_1 b_2 -> a_1 a_2 OR b_3 -> a_3
   
   
   
   complexity: O(n^2)
   
   
"""

class Solution87:
    pass
