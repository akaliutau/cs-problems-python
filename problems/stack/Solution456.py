"""   Given an array of n integers nums, a 132 pattern is a subsequence of three
   integers nums[i], nums[j] and nums[k] such that 
   i < j < k and 
   nums[i] < nums[k] < nums[j].
   
   Return true if there is a 132 pattern in nums, otherwise return false.
   
   Example 1:
   
   Input: nums = [1,2,3,4] Output: false Explanation: There is no 132 pattern in
   the sequence.
   
   IDEA:
   combination of prefix array and stack filtering
   [1,4,5,2]
    |   | \
   min  |  at stack
       cur
   
   the idea is to find a leftmost element (any) using a min prefix array 
   and an inverted pair (j, k) - use stack to hold all past values (== elem k) and current elem to find j
   
   1) min prefix array guarantee that there exists an elem which is smaller than the prefix elem at position i  
   2) stack guarantees the index of element on it is always bigger than the current one (past elements)
   3) for each element from tail check the condition elem > elem@stack
   
   
   
   1) first build a minimal stack
   look on the stack in 2 directions
   for each i
   one direction
    -->
   min number seen so far TO THE LEFT of i - check out min[i]
   
   
   
   <--
   2) use filtered stack which contains:
    values bigger than min[i]
   
   
   
"""

class Solution456:
    pass
