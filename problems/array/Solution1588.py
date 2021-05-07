"""   Given an array of positive integers arr, calculate the sum of all possible
   odd-length subarrays. A subarray is a contiguous subsequence of the array.
   Return the sum of all odd-length subarrays of arr. 
   
   Example 1: Input: arr = [1,4,2,5,3] Output: 58 
   
   Explanation: The odd-length subarrays of arr and their
   sums are: 
   [1] = 1 
     [4] = 4 
       [2] = 2 
         [5] = 5 
           [3] = 3 
   
   [1,4,2] = 7 
     [4,2,5] = 11
       [2,5,3] = 10 
       
   [1,4,2,5,3] = 15 
   
   If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
   
   IDEA:
   use prefix sum array and use it as cache of sums for subarryas with lengths = 5, 3, 1
   
    0  1  2  3  4   5
   [0, 1, 5, 7, 12, 15]
   
   
"""
from typing import List


class Solution1588:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        sum = [0] * (n+1)
        total = 0
        length = n-1 if n % 2 == 0 else n

        # prefix sum structure
        sum[0] = 0
        for i in range(0, n):
            sum[i] = sum[i-1] + arr[i]

        # start from the longest odd subsequence, down to the shortest one

        while length > 0:
            i = 0
            while i < n and i + length <= n:
                total += sum[i+length] - sum[i]
                i += 1
            length -= 2

        return total


