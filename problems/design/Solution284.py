"""   Implement iterator
   
   IDEA: 1) use 2 vars: hasNextCached & nextCached - to return value and state
   of iterator 2) change state only on next() invoking
   
   The solution will become very clear if to consider a PeekingIterator class as
   a state machine with two idempotent operations - peek() & hasNext() (state is
   not changed after call) and one operation which changes the inner state -
   next().
"""

class Solution284:
    pass
