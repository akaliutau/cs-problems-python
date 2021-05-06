"""   You are given two integer arrays nums1 and nums2 sorted in ascending order
   and an integer k. Define a pair (u,v) which consists of one element from the
   first array and one element from the second array. Find the k pairs
   (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums. 
   
   Example 1: Input: 
   nums1 = [1,7,11], nums2 = [2,4,6], k = 3 
   Output: [[1,2],[1,4],[1,6]] 
   
   Explanation: The first 3 pairs are returned from the sequence:
   [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
   
   it1 [1,2],[7,2],[11,2] - pick up [1,2], replace it with the next best candidate - [1,4]
"""

class Solution373:
    pass
