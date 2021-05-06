"""   Evaluate equation in string form
   
   f.e.
   
   3 - 2*2
   
    stack  num        numSign
    []      3            +  <-- this is what we are going to assign to number on the TOP OF STACK after number parsing
    [3]     null         -  <-- assign this to 2 after it's been parsed --- 
    [3]     2            -                                                 |
    [3, -2] null         *      <------------------------------------------
    [3, -2] 2            *  <-- apply this to 2 AND the top of stack, then put the result back to stack
    [3, -4] null 
           
    reduce [3, -4] -> -1
    
    IDEA:
    sign is always coming BEFORE number  
   
"""

class Solution227:
    pass
