"""   We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
   
   The number of (global) inversions is the number of i < j with 0 <= i < j < N
   and A[i] > A[j].
   
   The number of local inversions is the number of i with 0 <= i < N and A[i] >
   A[i+1].
   
   Return true if and only if the number of global inversions is equal to the
   number of local inversions.
   
   Example 1:
   
   Input: A = [1,0,2] Output: true Explanation: There is 1 global inversion, and
   1 local inversion.
  
   IDEA:
   1) any local inversion is a global inversion as well => in IdealPermutation all inversions are LOCAL
   2) if inversion is global only, one can return false immediately 
"""
from typing import List


class Solution775:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        max = 0
        for i in range(n-2):
            max = max(max,nums[i]) # the biggest number found so far
            if max > nums[i+2]:
                return False # if inversion is global only, one can return false immediately

        return True