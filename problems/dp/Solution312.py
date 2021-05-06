"""   Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
   number on it represented by array nums. You are asked to burst all the
   balloons. 
   If the you burst balloon       i 
   you will get     nums[left] * nums[i] * nums[right] coins. 
   
   Here left and right are adjacent indices of i. After the
   burst, the left and right then becomes adjacent. Find the maximum coins you
   can collect by bursting the balloons wisely. 
   
   Example: Input: [3,1,5,8]
   Output: 167 
   
   Explanation: nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> [] 
               coins =  3*1*5      +  3*5*8  +   1*3*8  +  1*8*1  = 167
               
     0  1 2 3 4  5, n = 6
     ========================          
     1 [3,1,5,8] 1
              |     |  
            left   right
      
            [3],[1],[5],[8]  - solve starting from [1] blocks        
          [3,1],[1,5],[5,8]
           [3,1,5],[1,5,8]
              [3,1,5,8] 
      
  """

class Solution312:
    pass
