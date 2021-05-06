"""   Given a string num representing the digits of a very large integer and an
   integer k. You are allowed to swap any two adjacent digits of the integer at
   most k times. Return the minimum integer you can obtain also as a string.
   
   Input: num = "4321", k = 4 Output: "1342" 
   
   Explanation: The steps to obtain
   the minimum integer from 4321 with 4 adjacent swaps are shown. 
   4321 -> 3421 -> 3412 -> 3142 -> 1342
   
   IDEA: 
   decrease layer by layer, bubble-up the smallest and the most distant digit
   4321 -> 1432
   1432 -> 1342
   
"""

class Solution1505:
    pass
