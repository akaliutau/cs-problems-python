"""   Given an integer array nums, you need to find one continuous subarray that if
   you only sort this subarray in ascending order, then the whole array will be
   sorted in ascending order. Return the shortest such subarray and output its
   leftgth. 
   
   Example 1: Input: nums = [2,6,4,8,10,9,15] Output: 5 
   
   Explanation: You
   need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array
   sorted in ascending order.
   
   IDEA: split the array into 3 parts:
   
   [inc][dec][inc]
       |     |
      left   right
      
   1) finding left boundary: for each segments like
            4
          /   \       
         /      3
        /        \
      1            2
            |   |
         hist > cur   <---   update left with index(hist)  
      
"""

class Solution581:
    pass
