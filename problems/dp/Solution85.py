"""   Given a rows x cols binary matrix filled with 0's and 1's, find the largest
   rectangle containing only 1's and return its area. 
   Input: matrix = [
   ["1","0","1","0","0"], 
   ["1","0","1","1","1"], 
   ["1","1","1","1","1"],
   ["1","0","0","1","0"]
   ] 
   
   Output: 6 Explanation: The maximal rectangle is shown in the above picture
   
   IDEA:
   Imagine an algorithm where for each point we computed a rectangle by doing the following:
   1) Finding the maximum height of the rectangle by iterating upwards until a 0 is reached
   2) Finding the maximum width of the rectangle by iterating outwards left and right
      until a height that doesn't accommodate the maximum height of the rectangle
      
   for each row use 2 pointers:
   left[i] - the last left edge of rectangle on the [0,i]
   right[i] - the last right edge of rectangle on the [i,n-1]
   height[i] - the best top edge of the bar on the [0,row]   
   
   left array for row 1
   ["0","0","2","0","0"], 
   ["0","4","2","4","4"], 
   h=1   0   1   0   0
   
   left array for row 2
   ["0","0","2","2","2"], 
   ["0","4","2","4","4"],
   h=2   0   2   1   1
    
   left array for row 3
   ["0","0","2","2","2"],
   ["4","4","2","4","4"]
   h=2   0   3   2   2
   
"""

class Solution85:
    pass
