"""   Given an array of integers and an integer k, you need to find the total
   number of continuous subarrays whose sum equals to k. 
   Example 1: Input:nums =
   [1,1,1], k = 2 Output: 2 sum array 
   
   [1,2,3] 
   
   The idea behind this approach is as follows: If
   the cumulative sum(represented by sum[i] for sum ith index) upto two indices
   is the same, the sum of the elements lying in between those indices is zero.
   Extending the same thought further, if the cumulative sum upto two indices,
   say i and j is at a difference: sum[i]−sum[j]=tgt, the sum of elements lying
   between indices i and j is tgt 
   
   We traverse over the array numsnums and keep
   on finding the cumulative sum. Every time we encounter a new sum, we make a
   new entry in the hashmap corresponding to that sum. If the same sum occurs
   again, we increment the count corresponding to that sum in the hashmap.
   
"""

class Solution560:
    pass
