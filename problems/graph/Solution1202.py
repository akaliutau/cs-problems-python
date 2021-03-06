"""   You are given a string s, and an array of pairs of indices in the string
   pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
   You can swap the characters at any pair of indices in the given pairs any
   number of times. Return the lexicographically smallest string that s can be
   changed to after using the swaps. 
   
   Example 1: Input: s = "dcab", pairs =
   [[0,3],[1,2]] Output: "bacd" Explaination: Swap s[0] and s[3], s = "bcad"
   Swap s[1] and s[2], s = "bacd"
   
   IDEA:
   1) build a network of connections
   2) for each node-letter: traverse through all tree and find the connected set
   3) sort and re-map all subsets
   
"""

class Solution1202:
    pass
