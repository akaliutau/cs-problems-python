"""   
   Array
   
   Given an array nums of n integers where n > 1, return an array output such
   that output[i] is equal to the product of all the elements of nums except
   nums[i].
   
   Example:
   
   Input: [1,2,3,4] Output: [24,12,8,6]
   
   
   IDEA: prefix product technique
   
   Instead of dividing the product of all the numbers in the array by the number
   at a given index to get the corresponding product, we can make use of the
   product of all the numbers to the left and all the numbers to the right of
   the index. Multiplying these two individual products would give us the
   desired result as well
   
"""
from typing import List


class Solution238:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        right = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * right
            right = right * nums[i]

        return res

