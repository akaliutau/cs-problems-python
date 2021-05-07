"""   Given an integer array of size n, find all elements that appear more than 
   n/3  times. Example 1: Input: nums = [3,2,3] Output: [3]
   
   [1,1,1,2,3,4,5]
   
   counter for 1:
    1 2 3 3 3 3 3 
   counter for 2:
          1 0 
            |
            2 => 3
    IDEA:
    use queue with fixed size (2 to be exact)
    
"""
from typing import List


class Solution229:
    def majorityElement(self, nums: List[int]) -> List[int]:

        stat = dict()
        for num in nums:
            if num in stat:
                stat[num] += 1
            else:
                stat[num] = 1

        n = len(nums)
        ans = []
        for key, val in stat.items():
            if val > n // 3:
                ans.append(key)

        return ans
