"""   Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
   surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in
   that surrounded region.
   
    Example: 
    X X X X 
    X O O X 
    X X O X 
    X O X X 
    
    After
   running your function, the board should be: 
   
   X X X X 
   X X X X 
   X X X X 
   X O X X
   
   IDEA:
   1) find all escaped cells using list of boundary cells and bfs from them (mark them temporarily as E)
   2) after run - convert all O -> X, and all E -> O
   
   
"""

class Solution130:
    pass
