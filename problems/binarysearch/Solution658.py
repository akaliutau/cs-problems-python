"""   Given a sorted array arr, two integers k and x, find the k closest elements
   to x in the array. The result should also be sorted in ascending order. If
   there is a tie, the smaller elements are always preferred.
   
   
   Example 1:
   
   Input: arr = [1,2,3,4,5], k = 4, x = 3 Output: [1,2,3,4]
   
   IDEA:
   the point is to find such mid that is the center of [mid, mid + k] - this will be the answer most close to the ideal one
   
   [1,2,3,4,5, 6] [1,3]
    |   |
    |  diff = -1 
    diff= 3
   
    0 1 2 3 4 5 6 7 8
   [1,2,3,4,5,6,7,8,9]
    |   |   |
    |  mid  r=n-4
   left
   
"""

class Solution658:
    pass
