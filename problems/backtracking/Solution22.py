"""   
   Given n pairs of parentheses, write a function to generate all combinations
   of well-formed parentheses.
   
   
   
   Example 1:
   
   Input: n = 3 Output: ["((()))","(()())","(())()","()(())","()()()"]
   
   IDEA:
   
   1) left branch - add ( until count < 3
   
   2) right branch - does not start until left branch exit
   
   
   			   ""
              /   \
             (     )
            / 
           (
          / \
         (   )
          \  | \
           ) (  )
            \
             )
              \
               )
         
"""
from typing import List


class Solution22:

    def _traverse(self, accumulator: List[int], s: str, open_count: int, close_count: int, n: int):
        if len(s) == 2 * n:
            accumulator.append(s)
        if open_count < n:
            self._traverse(accumulator, s + '(', open_count + 1, close_count, n)

        if open_count > close_count:
            self._traverse(accumulator, s + ')', open_count, close_count + 1, n)

    def generateParenthesis(self, n: int) -> List[str]:
        accumulator = []
        self._traverse(accumulator, "", 0, 0, n)

        return accumulator
