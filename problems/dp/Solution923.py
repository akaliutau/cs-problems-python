"""   Given an integer array arr, and an integer target, return the number of
   tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
   
   As the answer can be very large, return it modulo 109 + 7.
   
   Example 1:
   
   Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8 Output: 20
   
   Explanation: Enumerating by the values (arr[i], arr[j], arr[k]):
   
   (1, 2, 5) occurs 8 times;
   
   (1, 3, 4) occurs 8 times;
   
   (2, 2, 4) occurs 2 times;
   
   (2, 3, 3) occurs 2 times.
   
   IDEA:
   1) investigate all possibilities of [left, center, right] pairs
   1,1,2,2,3,3,4,4,5,5
   |     |     |
   left center  right
   
   
"""

class Solution923:
    pass
