"""   Least Recently Used (LRU) cache.
   https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU
   
   Design a data structure that follows the constraints of a Least Recently Used
   (LRU) cache.
   
   Implement the LRUCache class:
   
   LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
   int get(int key) Return the value of the key if the key exists, otherwise
   return -1. void put(int key, int value) Update the value of the key if the
   key exists. Otherwise, add the key-value pair to the cache. If the number of
   keys exceeds the capacity from this operation, evict the least recently used
   key.
   
   IDEA:
   use q queue with time ordering - the oldest nodes will be at the tail
   
   1) use a double-linked list to hold data
   2) on get: bubble up the requested node to the head
   3) on put:
     a) if exists - update the value and bubble up
     b) add new to the head and remove the oldest if needed
   
"""

class Solution146:
    pass
