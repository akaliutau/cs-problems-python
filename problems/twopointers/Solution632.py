"""   You have k lists of sorted integers in non-decreasing order. Find the
   smallest range that includes at least one number from each of the k lists. 
   
   We define the range [a, b] is smaller than range  [c, d] 
   if b - a < d - c or // shorter
   a < c if b - a == d - c. // leftmost if equals in length
   
   Example 1: Input: nums =  [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]] Output: [20,24] 
   
   Explanation: 
   List 1: [4, 10, 15, 24,26], 24 is in range [20,24]. 
   List 2: [0, 9, 12, 20], 20 is in range [20,24]. 
   List 3: [5, 18, 22, 30], 22 is in range [20,24]
   
   IDEA:
   for each k lists generate a ListElemTracker tracker
   then find interval = {Best{left_edge_i}, globalMaxAcrossAllLists}
   
   in the beginning:
   globalMaxAcrossAllLists for i=0 => max(4, 0, 5) = 5, =>
   [4,5]
   [0,5] - covers everything because 0 = (min across all intervals) (due to PriorityQueue feature)
   [5,5]
   
   On the second move the list #1 will be picked up with elem=4 and globalRight = 9
   i.e. we have a transition [0,5] -> [4,9] which is still covering all lines, i.e. replaced 5 -> 9 and 0 -> 4
   
   use PriorityQueue to pick  up the leftmost interval across all lists
   if the elem in some line is not present (f.e. 22 is not in [20,24], the process will be [20,22] -> [20,24])
"""

class Solution632:
    pass
