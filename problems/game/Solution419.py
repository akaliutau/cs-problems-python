"""   Given an 2D board, count how many battleships are in it. The battleships are
   represented with 'X's, empty slots are represented with '.'s. You may assume
   the following rules: You receive a valid board, made of only battleships or
   empty slots. Battleships can only be placed horizontally or vertically. In
   other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1
   (N rows, 1 column), where N can be of any size. At least one horizontal or
   vertical cell separates between two battleships - there are no adjacent
   battleships.
   
   IDEA:
   
   count those positions which belong to battleship (=='X'), and that's the
   bottom-right corner of the battleship (i.e., looking down and right from this
   cell we either go out of border, or see empty cell).
   
   
"""

class Solution419:
    pass
