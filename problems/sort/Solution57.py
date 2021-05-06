"""   Given a set of non-overlapping intervals, insert a new interval into the
   intervals (merge if necessary). You may assume that the intervals were
   initially SORTED according to their start times. 
   
   Example 1: Input: intervals
   = [[1,3],[6,9]], newInterval = [2,5] Output: [[1,5],[6,9]]
   
   IDEA:
   1) omit all arrays that ended before
   2) if array falls in gap, add it and replace newInterval with current one (all the rest will be chained)
   3) merge all intersection
   
   
   1st case - leave untouched
   
    [  ]
          [new]
   
   2nd case - the new starts before 1st overlapping/collision - add new and try to e
                         [    ]
                         
         [new]           |  
                         |
             |
       newInterval[1] <  in[0]  <-- then we switch to case 1 OR 3
   
   3rd case
            [    ]
         [new]
  
       [    ]
           [new]
  
"""

class Solution57:
    pass
