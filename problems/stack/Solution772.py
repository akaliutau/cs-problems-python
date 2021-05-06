"""   Implement a basic calculator to evaluate a simple expression string.
   
   The expression string contains only non-negative integers, +, -, *, /
   operators , open ( and closing parentheses ) and empty spaces . The integer
   division should truncate toward zero.
   
   You may assume that the given expression is always valid. All intermediate
   results will be in the range of [-2147483648, 2147483647].
   
   Follow up: Could you solve the problem without using built-in library
   functions.
   
   
   
   Example 1:
   
   Input: s = "1 + 1" Output: 2 Example 2:
   
   Input: s = " 6-4 / 2 " Output: 4
   
   IDEA:
   interpret blocks inside () using standard calc
     ( 1     8   )
     i i+1   j-1 j
   
    2-3/4
    
    stack
    +2
    -3
    /4
    
"""

class Solution772:
    pass
