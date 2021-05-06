"""   Given a linked list and a value x, partition it such that all nodes less than
   x come before nodes greater than or equal to x.
   
   You should preserve the original relative order of the nodes in each of the
   two partitions.
   
   Example:
   
   Input: head = 1->4->3->2->5->2, x = 3 
         Output: 1->2->2->4->3->5 
    
    note   1 -> 2 -> 2  [<-- before 3        after 3 -->]  4 -> 3 -> 5
                                                         order is preserved
   
   IDEA:
   use extra 2 LL to grow both lists
"""

class Solution86:
    pass
