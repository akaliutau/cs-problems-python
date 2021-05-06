"""   https://en.wikipedia.org/wiki/Least_frequently_used
   
   Design and implement a data structure for Least Frequently Used (LFU) cache.
   It should support the following operations: get and put.
   
   get(key) - Get the value (will always be positive) of the key if the key
   exists in the cache, otherwise return -1. put(key, value) - Set or insert the
   value if the key is not already present. When the cache reaches its capacity,
   it should invalidate the least frequently used item before inserting a new
   item. For the purpose of this problem, when there is a tie (i.e., two or more
   keys that have the same frequency), the least recently used key would be
   evicted.
   
   Note that the number of times an item is used is the number of calls to the
   get and put functions for that item since it was inserted. This number is set
   to zero when the item is removed.
   
   IDEA:
   use 2 structures to track nodes:
   1) map for fast access
   2) nodes grouped by frequency
   
   Note, that the tricky part is node migration (from group to group)
   
"""

class Solution460:
    pass
