"""   
   Given two sorted arrays nums1 and nums2 of size m and n respectively, return
   the median of the two sorted arrays
   
   Median definition
   
   The median of a finite list of numbers is the "middle" number, when those
   numbers are listed in order from smallest to greatest.
   
   If the data set has an odd number of observations, the middle one is
   selected. For example, the following list of seven numbers,
   
   1, 3, 3, 6, 7, 8, 9 has the median of 6, which is the fourth value.
            |
   
   If the data set has an even number of observations, the middle is
   an average of centroid. For example, the following list of seven numbers,
   
   1, 3, 3, 6, 7, 8, 9, 9 has the median 6.5.
            |  |
"""
from typing import List


class Solution4:

    def _merge(self, arr1: List[int], arr2 : List[int]) -> List[int]:
        res = []
        len1 = len(arr1)
        len2 = len(arr2)
        i = 0
        j = 0
        while i < len1 and j < len2:
            if arr1[i] >= arr2[j]:
                res.append(arr2[j])
                j += 1
            else:
                res.append(arr1[i])
                i += 1
        if i < len1:
            res += arr1[i:]
        if j < len2:
            res += arr2[j:]
        return res

    def _median(self, nums : List[int]) -> float:
        n = len(nums)
        if n % 2 == 1:
            return float(nums[n // 2])
        else:
            return (float(nums[n // 2 - 1]) + float(nums[n // 2])) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 == 0 and len2 == 0:
            return 0.0
        elif len1 == 0:
            return self._median(nums2)
        elif len2 == 0:
            return self._median(nums1)
        else:
            merged = self._merge(nums1, nums2)
            return self._median(merged)
