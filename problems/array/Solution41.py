"""   Given an unsorted integer array nums, find the smallest missing positive
   integer.
   
   Example 1:
   
   Input: nums = [1,2,0] Output: 3
   
   IDEA:
   
   
"""


class Solution41:

    def firstMissingPositive(self, nums):

        n = len(nums)
        has_one = False
        for num in nums:
            if num == 1:
                has_one = True

        if not has_one:
            return 1

        # nums length is 1, f.e  [1] - note it is ALWAYS 1 (due to the previous step)
        if n == 1:
            return 2

        # Replace negative numbers, zeros, and numbers larger than n by 1s.
        # After this nums will contain only positive numbers >= 1.

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        present = [False] * (n + 1)

        #  now we have only positive numbers >= 1
        # also now nums is a map, which maps to itself.

        for i in range(n):
            idx = nums[i]
            present[idx] = True

        for i in range(1, n + 1):
            if not present[i]:
                return i

        return n + 1
