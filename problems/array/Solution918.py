"""   Given a circular array C of integers represented by a, find the maximum
   possible sum of a non-empty subarray of C. 
   
   Here, a circular array means the
   end of the array connects to the beginning of the array. (Formally, C[i] =
   a[i] when 0 <= i < a.length, and C[i+a.length] = C[i] when i >= 0.) also, a
   subarray may only include each element of the fixed buffer a at most once.
   (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <=
   k1, k2 <= j with k1 % a.length = k2 % a.length.) 
   
   Example 1: Input:
   [1,-2,3,-2] Output: 3 Explanation: Subarray [3] has maximum sum 3
   
   
"""
from typing import List


class Solution918:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(gen: List[int]):
            ans = cur = - 2 ** 16 - 1
            for x in gen:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans

        S = sum(A)
        ans1 = kadane(iter(A))

        arr2 = [-A[i] for i in range(1, len(A))]
        ans2 = S + kadane(arr2)

        arr3 = [-A[i] for i in range(len(A) - 1)]
        ans3 = S + kadane(arr3)
        return max(ans1, ans2, ans3)