"""   Given a set of distinct integers, nums, return all possible subsets (the
   power set). Note: The solution set must not contain duplicate subsets.
   Example: 
   Input: nums = [1,2,3] 
   Output: 
   [
   
    [3], 
    [1], 
    [2], 
    
    [1,2,3], 
    
    [1,3],
    [2,3], 
    [1,2], 
    
    [] 
    
   ]
   
   IDEA:
   [] -> [1], [2], [3] - generate initial set,
   then use this set to append the next available number: 
   [1] -> [1,2], [1,3], and so on
   
"""

class Solution78:
    pass
