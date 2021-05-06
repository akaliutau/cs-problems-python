"""   Given an array nums which consists of non-negative integers and an integer m,
   you can split the array into m non-empty continuous subarrays. Write an
   algorithm to minimize the largest sum among these m subarrays. 
   
   Example 1:
   Input: nums = [7,2,5,10,8], m = 2 Output: 18 
   
   Explanation: There are four ways
   to split nums into two subarrays. The best way is to split it into [7,2,5]
   and [10,8], where the largest sum among the two subarrays is only 18.
   
   [7,2,5,10,8] = 
   [7] + SUM[2,5,10,8]
   [7,2] + SUM[5,10,8]
   [7,2,5] + SUM[10,8]
   [7,2,5,10] + SUM[8]
   
"""

class Solution20:
    pass
