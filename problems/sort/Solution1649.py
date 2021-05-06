"""   Given an integer array instructions, you are asked to create a sorted array
   from the elements in instructions. You start with an empty container nums.
   For each element from left to right in instructions, insert it into nums. 
   
   The cost of each insertion is the minimum of the following: 
   
   1) The number of elements currently in nums that are strictly less than instructions[i]. 
   
   2) The number of elements currently in nums that are strictly greater than
   instructions[i]. 
   
   For example, if inserting element 3 into nums = [1,2,3,5],
   the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element
   5 is greater than 3) and nums will become [1,2,3,3,5]. 
   
   Return the total cost
   to insert all elements from instructions into nums. Since the answer may be
   large, return it modulo 109 + 7
   
   Example 1: Input: instructions = [1,5,6,2]
   Output: 1 
   
   
   Explanation: Begin with nums = []. 
   Insert 1 with cost min(0, 0) = 0, now nums = [1]. 
   Insert 5 with cost min(1, 0) = 0, now nums = [1,5]. 
   Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6]. 
   Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6]. 
   The total cost is 0 + 0 + 0 + 1 = 1.
   
   IDEA 1: https://en.wikipedia.org/wiki/Fenwick_tree
   IDEA 2:
   
   1) build a BST for arr=[1,5,6,2]
   
            5
           / \
          2   6       <--- if we are traversing BST for elem 2, we have to add all bigger elements at point 5, i.e. right branch
         /
        1  
   
   2) for (each elem in arr):
      A. find its exact location on the tree O(log n)
      B. during traversal mark the path along the way - as a result we will know at any point of time, 
      how many times this node has been crossed in the past. Also this information about underlying nodes helps to
      figure out number of crossed nodes SMALLER and BIGGER than the current one (due to props of BST)
   
   	  For example, at the end of full arr processing the node's crossCount will be:
   
       crossCount | node
       -----------------
       4             5
       2             2
       1             1
       1             6
       
       So we can know precisely for 5: exist 2 elems less and 1 elem bigger
     
    O(n log n) 
"""

class Solution1649:
    pass
