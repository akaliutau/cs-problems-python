"""   You are given an integer array nums. The unique elements of an array are the
   elements that appear exactly once in the array.
   
   Return the sum of all the unique elements of nums.
   
   
   
   Example 1:
   
   Input: nums = [1,2,3,2] Output: 4 Explanation: The unique elements are [1,3],
   and the sum is 4.
  
"""
from typing import List


class Solution1748:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = set()
        unique = set()
        for num in nums:
            unique.add(num)
            if num in seen:
                unique.remove(num)
            seen.add(num)

        return sum(unique)
