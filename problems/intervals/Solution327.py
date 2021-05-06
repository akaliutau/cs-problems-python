"""   Given an integer array nums, return the number of range sums that lie in
   [lower, upper] inclusive. Range sum S(i, j) is defined as the sum of the
   elements in nums between indices i and j (i ≤ j), inclusive. Note: A naive
   algorithm of O(n2) is trivial. You MUST do better than that. 
   
   Example: Input:
   nums = [-2,5,-1], lower = -2, upper = 2, Output: 3 
   
   Explanation: The three
   ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
   Constraints: 0 <= nums.length <= 10^4 
   
   IDEA: the second for loop in BF approach is used to
   find the number of j that satisify: 
   lower <= presum[i] - presum[j] <= upper 
   ==> 
   presum[i] - upper <= presum[j] <= presum[i] - lower 
   
   We need to find out how many j satisifies this condition.
   
   If we store the presum[] sorted, we can easily find the position of presum[i]
   - upper and presum[i] - lower. 
   
   So the number of satisified j will be count(pos2 - pos1) 
   
   We could get the API from the code above: add(value): add
   a value into a data structure query(): query how many numbers of values in
   this range 
   
   This is very close to Segment Tree
"""

class Solution327:
    pass
