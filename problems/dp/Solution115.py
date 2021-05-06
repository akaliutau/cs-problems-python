"""   Given two strings s and t, return the number of distinct subsequences of s
   which equals t. A string's subsequence is a new string formed from the
   original string by deleting some (can be none) of the characters without
   disturbing the relative positions of the remaining characters. (i.e., "ACE"
   is a subsequence of "ABCDE" while "AEC" is not). It's guaranteed the answer
   fits on a 32-bit signed integer. 
   
   Example 1: Input: s = "rabbbit", t = "rabbit" Output: 3 
   
   Explanation: As shown below, there are 3 ways you can
   generate "rabbit" from S.
   ____ __ 
   rabbbit 
   
   __ ____
   rabbbit 
   
   ___ ___
   rabbbit
   
   IDEA:
   lets t=ra, s=ram
   
   if we have a sequence
   [ra]
   number of distinct subsequences, layer by layer:
   
   i=0, t="",   [""]  ["r"]  ["ra"]  ["ram"]
                    \
   i=1, t="r",  [""]<-["r"]<-["r"]<- ["r"]
       
   i=2, t="ra", [""]<-["r"]<-["r"]<- ["r"]
   
   where
   \ = use data from previous iteration, like this
   
   ["", r, a, ra] = [{"",r} + {"",r} * a]
   
   <- = copy prev result-set
    
   ["", r, a, ra] --> ["", r, a, ra]
   
   
"""

class Solution115:
    pass
