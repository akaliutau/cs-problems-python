"""   Given an unsorted array, find the maximum difference between the successive
   elements in its sorted form. Return 0 if the array contains less than 2
   elements. 
   
   Example 1: Input: [3,6,9,1] Output: 3 Explanation: The sorted form
   of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference
   3.
   
   IDEA:
   sort and compare pairs [i] and [i+1]
"""
from typing import List


class Solution164:
    def maximumGap(self, nums : List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        nums.sort()
        diff = nums[1] - nums[0]
        i = 1
        while i < n - 1:
            diff = max(diff, nums[i+1] - nums[i])
            i += 1
        return diff
