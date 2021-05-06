"""   Given an integer array nums, find the sum of the elements between indices i
   and j (i ≤ j), inclusive. The update(i, val) function modifies nums by
   updating the element at index i to val. 
   
   Example: Given nums = [1, 3, 5]
   sumRange(0, 2) -> 9 update(1, 2) sumRange(0, 2) -> 8 
   
   Segment tree is a very
   flexible data structure, because it is used to solve numerous range query
   problems like finding minimum, maximum, sum, greatest common divisor, least
   common denominator in array in logarithmic time. 
   
   The segment tree for array
   a[0, 1, ... ,n-1] is a binary tree in which each node contains aggregate
   information (min, max, sum, etc.) for a subrange [i ... j] of the array, as
   its left and right child hold information for range [i ... {i+j}/2] and
   [{i+j}/2 + 1, j] 
   
   Segment tree could be implemented using either an array or a
   tree. For an array implementation, if the element at index ii is not a leaf,
   its left and right child are stored at index 2i and 2i + 1 respectively.
"""

class Solution307:
    pass
