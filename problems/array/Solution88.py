"""   
   Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
   one sorted array.
   
   Note:
   
   The number of elements initialized in nums1 and nums2 are m and n
   respectively. You may assume that nums1 has enough space (size that is equal
   to m + n) to hold additional elements from nums2. Example:
   
   Input: nums1 = [1,2,3,0,0,0], m = 3 nums2 = [2,5,6], n = 3
   
   Output: [1,2,2,3,5,6]
   
   IDEA: merge starting from the end for both result and 2 merge pointers
   
"""

class Solution88:
    def merge(self, nums1, m, nums2, n):
        pos1 = m - 1
        pos2 = n - 1
        at = pos1
        while at >= 0:
            if pos1 >= 0 and pos2 >= 0:
                if nums1[pos1] > nums2[pos2]:
                    nums1[at] = nums1[pos1]
                    pos1 -= 1
                else:
                    nums2[at] = nums2[pos2]
                    pos2 -= 1
            elif pos1 >=0:
                nums1[at] = nums1[pos1]
                pos1 -= 1
            elif pos2 >=0:
                nums1[at] = nums2[pos2]
                pos2 -= 1
            at -= 1



