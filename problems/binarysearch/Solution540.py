"""   You are given a sorted array consisting of only integers where every element
   appears exactly twice, except for one element which appears exactly once.
   Find this single element that appears only once. Follow up: Your solution
   should run in O(log n) time and O(1) space. 
   
   Example 1: Input: nums =
   [1,1,2,3,3,4,4,8,8] Output: 2
   
   [1,1,2,3,3,4,4,8,8]
    |               |
    l(0)            r(8)
      
   [1,1,2,3,3,4,4,8,8]
    |       |       |
            mid(4) != mid +1 => missing number is to the left of mid!
            
"""

class Solution540:
    pass
