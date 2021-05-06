"""   There is a new alien language which uses the latin alphabet. 
   However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, 
   where words are sorted lexicographically by the rules of this new language.
   Derive the order of letters in this language.
   
   IDEA: 
   1) extract partial relations from known words 
   2) topologically sort them 
   3) output ordered letters 
   
   Input: [ "wrt", "wrf", "er", "ett", "rftt" ] 
   Output: "wertf"
   
   1) partial relations: 
      w->e, e->r,(1st letter)   t->f (3rd letter), r->t (2nd letter, er-ett)
   2) ordered:
      w->e, e->r, r->t, t->f
   3)  wertf     
       
"""

class Solution269:
    pass
