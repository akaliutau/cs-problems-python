"""   Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
   
   IDEA:
   use auxiliary structure to track the number of elements found in the original array
   
"""


class Solution80:
    def removeDuplicates(self, nums):
        mapped = [0] * 20002
        pos = 0
        for num in nums:
            if mapped[num + 10000] < 2:
                nums[pos] = num
                pos += 1
                mapped[num + 10000] += 1

        return pos
