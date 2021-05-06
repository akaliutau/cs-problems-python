"""   Implement a basic calculator to evaluate a simple expression string.
   
   The expression string may contain open ( and closing parentheses ), the plus
   + or minus lastSign -, non-negative integers and empty spaces .
   
   Example 3:
   
   Input: "(1+(4+5+2)-3)+(6+8)" Output: 23
   
   IDEA: 
   look at the following symbols  +,- & ), \n as terminal operation
   
   
   
         4+5+2                           <--- stack level 2
     1+ (     )-3    6 + 8               <--- stack level 1
   (             )+(       )             <--- stack level 0
   
   save parsed sign to lastSign
   save parsed operand to lastOperand
   operations '-', '+' triggers the procedure of accumulator update
"""

class Solution224:
    pass
