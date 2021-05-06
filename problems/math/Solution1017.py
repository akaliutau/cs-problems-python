"""   Given a number N, return a string consisting of "0"s and "1"s that represents
   its value in base -2 (negative two).
   
   The returned string must have no leading zeroes, unless the string is "0".
   
   
   
   Example 1:
   
   Input: 2 Output: "110" Explanation: (-2) ^ 2 + (-2) ^ 1 = 2
   
   IDEA:
   Approach absolutely the same as that for converting numbers on the basis = base
   
   Proof:
   
           (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 2  <-- divide both parts on base = -2
           1           1          0            <-- how many pieces must be added 
           
   1) Each time after dividing number by -2 we get an answer as a reminder
   2) if  reminder < 0, => base is < 0     
    
  
"""

class Solution1017:
    pass
