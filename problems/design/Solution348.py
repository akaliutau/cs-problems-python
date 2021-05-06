"""   Assume the following rules are for the tic-tac-toe game on an n x n board
   between two players:
   
   A move is guaranteed to be valid and is placed on an empty block. Once a
   winning condition is reached, no more moves are allowed. A player who
   succeeds in placing n of their marks in a horizontal, vertical, or diagonal
   row wins the game. Implement the TicTacToe class:
   
   TicTacToe(int n) Initializes the object the size of the board n. int move(int
   row, int col, int player) Indicates that player with id player plays at the
   cell (row, col) of the board. The move is guaranteed to be a valid move.
   
   IDEA:
   each player either increase by 1 the cell or descrease it
   if some row| column | diag  reach sum with norm == ||n|| someone won
   
"""

class Solution348:
    pass
