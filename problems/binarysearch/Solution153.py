"""   
   Suppose an array sorted in ascending order is rotated at some pivot unknown
   to you beforehand.
   
   (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
   
   Find the minimum element.
   
   You may assume no duplicate exists in the array.
   
   Example 1:
   
   Input: [3,4,5,1,2] Output: 1
   
    IDEA: min elem = point of change
    
    
   CASE 1
   [4,5,6,7,0,1,2]
          |
          7>0 - then this is the point of change
   
   CASE 2        
   [4,5,6,7,0,1,2]
        |
        6>4  point of changes somewhere on the right piece
        
"""

class Solution153:
    pass
