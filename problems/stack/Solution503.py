"""   
   Given a circular array (the next element of the last element is the first
   element of the array), print the Next Greater Number for every element. The
   Next Greater Number of a number x is the first greater number to its
   traversing-order next in the array, which means you could search circularly
   to find its next greater number. If it doesn't exist, output -1 for this
   number.
   
   
   Input: [1,2,1] (circular array) Output: [2,-1,2]
   
   Explanation: The first 1's next greater number is 2; The number 2 can't find
   next greater number; The second 1's next greater number needs to search
   circularly, which is also 2.
   
   IDEA:
   use stack to hold only those elements which are > current
   
   array              stack     result
   -------------------------------------------
   [1, 2,  1]        []        [0,0,-1]
           |
           
   [1, 2,  1]        [2]       [0,-1,-1] <-- '1' has been removed, '2' was added during normal cycle
       |
           
   [1, 2,  1]        [2,1]     [2,-1,-1] <-- first hit, '1' was added during normal cycle
    |
    
   In order to get the correct answer, the 2nd round is needed
    
   [1, 2,  1]        [2,1]     [2,-1, 2] <-- second hit, first '1' has been removed, then last '1' was added during normal cycle
           |
    and so on
           
   T(2n + n)
   
"""

class Solution503:
    pass
