"""   Given a positive integer n, you can apply one of the following operations: If
   n is even, replace n with n / 2. If n is odd, replace n with either n + 1 or
   n - 1. Return the minimum number of operations needed for n to become 1.
   
   Example 1: Input: n = 8 Output: 3 Explanation: 8 -> 4 -> 2 -> 1
   
   IDEA:
   combination of BFS with recursion
   
   1) Use BFS on all possibilities for current Number
   2) Use memoization for cache for already calculated numbers
   
   time: O(3n) ~ O(n), because ((curr+1)+1) became divisible by 2
   
   
   
"""

class Solution397:
    pass
