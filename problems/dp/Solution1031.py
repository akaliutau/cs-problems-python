"""   Given an array arr of non-negative integers, return the maximum sum of
   elements in two non-overlapping (contiguous) subarrays, which have lengths L
   and M. (For clarification, the L-length subarray could occur before or after
   the M-length subarray.) Formally, return the largest V for which 
   V = (arr[i] + arr[i+1] + ... + arr[i+L-1]) + 
       (arr[j] + arr[j+1] + ... + arr[j+M-1]) and
   either: 
   0 <= i < (i + L - 1) < j < (j + M - 1) < arr.length, or 
   0 <= j < (j + M - 1) < i < (i + L - 1) < arr.length. 
   
   Example 1: Input: arr = [0,6,5,2,2,5,1,9,4],
   L = 1, M = 2 Output: 20 
   
   Explanation: One choice of subarrays is [9] with length 1, 
                                       and [6,5] with length 2. 
   
   Example 2: Input: arr =
   [3,8,1,3,2,1,8,9,0], L = 3, M = 2 Output: 29 
   
   [3, 8,  1, 3,2, 1, 8, 9, 0]
   
   dpL:
   [12,12, 6, 6,11,18,17,9, 0]
   [18,18,18,18,18,18,17,9, 0]
   
   
   Explanation: One choice of
   subarrays is [3,8,1] with length 3, and [8,9] with length 2.
"""

class Solution1031:
    pass
