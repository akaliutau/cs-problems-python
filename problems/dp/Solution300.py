"""   Given an unsorted array of integers, find the length of longest increasing
   subsequence. Example: Input: [10,9,2,5,3,7,101,18] Output: 4 
   
   Explanation: The
   longest increasing subsequence is [2,3,7,101], therefore the length is 4.
   
   This method relies on the fact that the longest increasing subsequence
   possible upto the ith index in a given array is independent of the
   elements coming later on in the array. Thus, if we know the length of the LIS
   upto i th index, we can figure out the length of the LIS possible by
   including the (i+1)th elem
   
   O(n^2)
"""

class Solution300:
    pass
