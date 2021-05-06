"""   A kingdom consists of a king, his children, his grandchildren, and so on.
   Every once in a while, someone in the family dies or a child is born. The
   kingdom has a well-defined order of inheritance that consists of the king as
   the first member. Let's define the recursive function Successor(x, curOrder),
   which given a person x and the inheritance order so far, returns who should
   be the next person after x in the order of inheritance. Successor(x,
   curOrder): if x has no children or all of x's children are in curOrder: if x
   is the king return null else return Successor(x's parent, curOrder) else
   return x's oldest child who's not in curOrder 
   
   For example, assume we have a
   kingdom that consists of the king, his children Alice and Bob (Alice is older
   than Bob), and finally Alice's son Jack. 
   
   In the beginning, curOrder will be ["king"]. 
   Calling Successor(king, curOrder) will return Alice, so we append to curOrder to get ["king", "Alice"]. 
   
   Calling Successor(Alice, curOrder) will return Jack, so we append to curOrder to get ["king", "Alice", "Jack"].
   Calling Successor(Jack, curOrder) will return Bob, so we append to curOrder to get ["king", "Alice", "Jack", "Bob"]. 
   Calling Successor(Bob, curOrder) will return null. Thus the order of inheritance will be ["king", "Alice", "Jack", "Bob"].
   
   IDEA:
   use static tree and update it with flag isAlive=false if person died (use this flag to build a hierarchy)
   
"""

class Solution1600:
    pass
