"""   You have a bomb to defuse, and your time is running out! Your informer will
   provide you with a circular array code of length of n and a key k. To decrypt
   the code, you must replace every number. All the numbers are replaced
   simultaneously. 
   
   If k > 0, replace the ith number with the sum of the next k numbers. 
   
   If k < 0, replace the ith number with the sum of the previous k numbers. 
   
   If k == 0, replace the ith number with 0. As code is circular, the
   next element of code[n-1] is code[0], and the previous element of code[0] is
   code[n-1]. 
   
   Given the circular array code and an integer key k, return the
   decrypted code to defuse the bomb! 
   
   Example 1: Input: code = [5,7,1,4], k = 3 Output: [12,10,16,13] 
   
   Explanation: Each number is replaced by the sum of the
   next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice
   that the numbers wrap around.
"""
from typing import List


class Solution1652:
    def decrypt(self, code:List[int], k:int) -> List[int]:
        n = len(code)
        decoded = [0] * n
        if k == 0:
            return decoded
        sum = [0] * n; # sum_i = sum(i,i+k-1) exclusive
        kSum = 0
        # calc the very first sum

        l = abs(k)
        for i in range(l):
            kSum += code[i % n]
        sum[0] = kSum
        for i in range(1,n):
            less = code[i-1]
            more = code[(i + l - 1) % n]
            kSum += (more - less)
            sum[i] = kSum
        if k > 0:
            for i in range(n):
                decoded[i] = sum[(i + 1) % n]
        else:
            for i in range(n):
                decoded[(l + i) % n] = sum[i]
        return decoded
