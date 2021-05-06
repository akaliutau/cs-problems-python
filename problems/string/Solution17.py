"""   Given a string containing digits from 2-9 inclusive, 
   return all possible letter combinations that the number could represent. Return the answer in any order.
   
   IDEA:
   Generates a list of possibilities using prefix like "abc" and suffices from all previous steps
   
   1st iteration: [] -> [a, b, c]
   1st iteration: [a, b, c] -> [aa, ba, ca, ab, bb, cb, ac, bc, cc] - Cartesian multiplication
   
"""

class Solution17:
    pass
