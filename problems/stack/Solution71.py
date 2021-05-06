"""   
   Given an absolute path for a file (Unix-style), simplify it. Or in other
   words, convert it to the canonical path.
   
   In a UNIX-style file system, a period . refers to the current dir.
   Furthermore, a double period .. moves the dir up a level.
   
   Note that the returned canonical path must always begin with a slash /, and
   there must be only a single slash / between two dir names. The last
   dir name (if it exists) must not end with a trailing /. Also, the
   canonical path must be the shortest string representing the absolute path.
   
   
   
   Example 1:
   
   Input: "/home/" Output: "/home" Explanation: Note that there is no trailing
   slash after the last dir name.
   
   IDEA:
   Straightforward: use '.' or '..' sequence names as COMMANDS
   
"""

class Solution71:
    pass
