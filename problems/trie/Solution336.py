"""   Given a list of unique words, return all the pairs of the distinct indices
   (i, j) in the given list, so that the concatenation of the two words words[i]
   + words[j] is a palindrome. 
   
   Example 1: Input: words = ["abcd","dcba","lls","s","sssll", "ka"] 
   Output: [[0,1],[1,0],[3,2],[2,4]]
   
   Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
   
   IDEA:
   dcbaabcd = [dc][baab][cd]
   
   [dc]~[cd]
   [ba]~[ab]
   
   
   dcbaabcd = [dcb] + [aabcd]
       8        3        5
       
              [dcb]   [dcbaa]      
              prefix  prefix + palindrome   
                3       3        from 3
            ending=3  ending=5            
        prefixLi=[5]  prefixLi=[]           
   
"""

class Solution336:
    pass
