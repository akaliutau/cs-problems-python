"""   Serialization is the process of converting a data structure or object into a
   sequence of bits so that it can be stored in a file or memory buffer, or
   transmitted across a network connection link to be reconstructed later in the
   same or another computer environment.
   
   Design an algorithm to serialize and deserialize a binary tree. There is no
   restriction on how your serialization/deserialization algorithm should work.
   You just need to ensure that a binary tree can be serialized to a string and
   this string can be deserialized to the original tree structure.
   
   IDEA:
   1) serialize: save nodes as they are traversed, incl. the empty ones (null)
   2) deserialize: use the same traversing order and feed deserializer with data from file
   
"""

class Solution297:
    pass
