"""
Given an integer array nums, return true
if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

IDEA:

   [2,1,5,0,4,6]
    |   |     |
  left  mid            |
  iterate the last elem only and use "seen numbers" flow

  2
  1
  5 1
  5 0 <- decreasing the left element does not change the topology, but opens the door for new triad
  4 0 <- decreasing the mid element does not change the topology, but boosts chances to find the 3rd (lowers the bar)

"""
from typing import List


class Solution:
    def increasing_triplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        left = 2 ** 31
        mid = 2 ** 31
        for cur in nums:
            if left < mid < cur:  # exit condition
                return True
            if left < cur:  # find the left pair
                mid = cur
            elif left > cur:  # left is always the smallest number seen so far
                left = cur
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.increasing_triplet([2, 1, 5, 0, 6, 6]))
