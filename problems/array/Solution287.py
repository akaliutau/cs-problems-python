"""   Given an array of integers nums containing n + 1 integers where each integer
   is in the range [1, n] inclusive. There is only one duplicate number in nums,
   return this duplicate number. Follow-ups: How can we prove that at least one
   duplicate number must exist in nums? Can you solve the problem without
   modifying the array nums? Can you solve the problem using only constant, O(1)
   extra space? Can you solve the problem with runtime complexity less than
   O(n2)? 
   
   Example 1: Input: nums = [1,3,4,2,2] Output: 2 
   
   
   Example 2: Input: nums = [3,1,3,4,2] Output: 3
   
   IDEA: nums is a group
   lets nums is an array of ref, double means a cycle
"""
from typing import List


class Solution287:
    def findDuplicate(self, nums: List[int]) -> int:
        first_ptr = nums[0]
        second_ptr = nums[0]
        first_ptr = nums[first_ptr]
        second_ptr = nums[nums[second_ptr]]
        while first_ptr != second_ptr:
            first_ptr = nums[first_ptr]
            second_ptr = nums[nums[second_ptr]]

        # This part in needed  because the intersection point is not the cycle entrance in the general case
        # For example
        # [1,3,4,2,2]
        #  0 1 2 3 4 <-- path + oscillator with length < n
        #  to determine the
        #  1 -> 3 -> 2 -> 4 -> 2
        #  1 -> 4 -> 4 -> 4

        # [2,5,9,6,4,3,8,9,7,1]

        ptr1 = nums[0]
        ptr2 = first_ptr  # intersection
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

