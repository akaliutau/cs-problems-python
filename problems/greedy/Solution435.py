"""   Given a collection of intervals, find the minimum number of intervals you
   need to remove to make the rest of the intervals non-overlapping. Example 1:
   Input: [[1,2],[2,3],[3,4],[1,3]] Output: 1 Explanation: [1,3] can be removed
   and the rest of intervals are non-overlapping.
   
   IDEA:
    consider continuous removal: 
    1) collect the statistics about overlaps for each interval
    2) sort them
    [1,2],[2,3],[3,4],[1,3] =>
    
    [1,2],[1,3],[2,3],[3,4]
    
    
    O(n^2) for stat
    O(n^2) for iterative removal
"""

class Solution435:
    pass
