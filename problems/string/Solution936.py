"""   You want to form a target string of lowercase letters.
   
   At the beginning, your sequence is target.length '?' marks. You also have a
   stamp of lowercase letters.
   
   On each turn, you may place the stamp over the sequence, and replace every
   letter in the sequence with the corresponding letter from the stamp. You can
   make up to 10 * target.length turns.
   
   For example, if the initial sequence is "?????", and your stamp is "abc",
   then you may make "abc??", "?abc?", "??abc" in the first turn. (Note that the
   stamp must be fully contained in the boundaries of the sequence in order to
   stamp.)
   
   If the sequence is possible to stamp, then return an array of the index of
   the left-most letter being stamped at each turn. If the sequence is not
   possible to stamp, return an empty array.
   
   For example, if the sequence is "ababc", and the stamp is "abc", then we
   could return the answer [0, 2], corresponding to the moves "?????" -> "abc??"
   -> "ababc".
   
   Also, if the sequence is possible to stamp, it is guaranteed it is possible
   to stamp within 10 * target.length moves. Any answers specifying more than
   this number of moves will not be accepted.
   
   
   
   Example 1:
   
   Input: stamp = "abc", target = "ababc" Output: [0,2] ([1,0,2] would also be
   accepted as an answer, as well as some other answers.)
   
   IDEA:
   Start filling target array with ? from the top to the down
   
   | | | |a|b|c| | |  <-- 3 exact matches
   | |a|b|?|?|?| | |  <-- 2 exact matches, 1 ?
   | | | | | |?|b|c|  <-- 2 exact matches, 1 ?
   |a|b|c| | | | | |  <-- 1 exact matches, 2 ?
    
   Filter out all cases when exactMatch[best] + q[best] < m || all exact matches < m, etc
  
"""

class Solution936:
    pass
