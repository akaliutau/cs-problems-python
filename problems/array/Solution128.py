"""   Given an unsorted array of integers, find the length of the longest
   consecutive elements sequence. Your algorithm should run in O(n) complexity.
   
   Example: Input: [100, 4, 200, 1, 3, 2] Output: 4 Explanation: The longest
   consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4
   
   IDEA: find the beginning of some sequence
   as a result the total time complexity will be O(n) - if contains operation is O(1)
"""


class Solution128:
    def longestConsecutive(self, nums):
        num_set = set(nums)

        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                currentNum = num
                curSubseq = 1  # num is an elem

                while currentNum + 1 in num_set:
                    currentNum += 1
                    curSubseq += 1
                # update longest length
                longest_streak = max(longest_streak, curSubseq)

        return longest_streak