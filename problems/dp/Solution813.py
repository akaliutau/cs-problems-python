"""   We partition a row of numbers a into at most k adjacent (non-empty) groups,
   then our score is the sum of the average of each group. What is the largest
   score we can achieve? note that our partition must use every number in a, and
   that scores are not necessarily integers. 
   
   Example: Input: a = [9,1,2,3,9] k = 3 Output: 20 
   
   Explanation: The best choice is to partition a into [9], [1, 2, 3], [9]. 
   The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20. We could have also
   partitioned a into [9, 1], [2], [3, 9], for example. That partition would
   lead to a score of 5 + 2 + 6 = 13, which is worse
"""

class Solution813:
    pass
