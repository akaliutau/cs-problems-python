"""   There are n servers numbered from 0 to n-1 connected by undirected
   server-to-server connections forming a network where connections[i] = [a, b]
   represents a connection between servers a and b. Any server can reach any
   other server directly or indirectly through the network.
   
   A critical connection is a connection that, if removed, will make some server
   unable to reach some other server.
   
   Return all critical connections in the network in any order
   
   IDEA:
   critical conn = node which has been passed twice (at least)
   1) relaxation decrease min time to the lowest time on the loop (if any)
    f.e. A->B->C->A
         1  2  3  1
         1  1  1  1
         C->D
         1  4
         
         A, B, C - form a cycle
         D - a separate node
"""

class Solution1192:
    pass
