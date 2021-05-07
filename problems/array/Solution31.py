"""   Implement next permutation, which rearranges numbers into the
   lexicographically next greater permutation of numbers. If such an arrangement
   is not possible, it must rearrange it as the lowest possible order (i.e.,
   sorted in ascending order). The replacement must be in place and use only
   constant extra memory. Example 1: Input: nums = [1,2,3] Output: [1,3,2]
   
   [1,3,5,4]
   [1,4,5,3] -> [1,4,3,5] reverse
   
   IDEA:
   0) represent visually a number as a histogram 
   1) find a peak 
   2) the NEXT greater number obviously must be a number created from this one by 
      a) finding the smallest possible change - can be done by searching from the tail backwards
      b) swapping these elements  
   3) reversing the tail AFTER peak (including peak) is needed due to guaranteed smallest number  
   
"""

class Solution31:

    def _reverse(self, nums, idx):  # reverses[1, 2, 3] -> [3, 2, 1]
        print(nums, idx)
        i = idx
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:  # find a peak in a histogram - an asc order from the tail
            i -= 1
        # now [i+1] is the peak, [i] - the elem just before the peak

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:  # find the 1st elem greater or equal than found one
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        self._reverse(nums, i + 1);


