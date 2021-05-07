"""   Given a non-empty array of integers, return the third maximum number in this
   array. If it does not exist, return the maximum number. The time complexity
   must be in O(n). 
   
   Example 1: Input: [3, 2, 1] Output: 1 Explanation: The third
   maximum is 1.
   
   IDEA:
   introduce a limit for max function
   
"""
from typing import List, final


class Solution414:

    max_int = 2 ** 32 - 1
    min_int = -max_int

    def _find(self, nums: List[int], ceil : int):
        max_val = self.min_int
        for num in nums:
            if max_val < num < ceil:
                max_val = num

        return max_val

    def thirdMax(self, nums: List[int]) -> int:
        first = self._find(nums, self.max_int)
        second = self._find(nums, first)
        if second == self.min_int:
            return first

        third = self._find(nums, second)
        if third == self.min_int:
            return first

        return third