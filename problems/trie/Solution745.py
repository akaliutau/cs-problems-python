"""   Design a special dictionary which has some words and allows you to search the
   words in it by a prefix and a suffix.
   
   Implement the WordFilter class:
   
   WordFilter(string[] words) Initializes the object with the words in the
   dictionary. f(string prefix, string suffix) Returns the index of the word in
   the dictionary which has the prefix prefix and the suffix suffix. If there is
   more than one valid index, return the largest of them. If there is no such
   word in the dictionary, return -1.
   
   
   Example 1:
   
   Input ["WordFilter", "f"] [[["apple"]], ["a", "e"]] Output [null, 0]
   
   Explanation WordFilter wordFilter = new WordFilter(["apple"]);
   wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix =
   "a" and suffix = 'e".
   
   IDEA:
   1) Maintain 2 tries: for prefixes and the 2nd one - for the reverse suffixes
   2) for each word remember the sorted list of matched words
   3) find the biggest number in intersection
   
"""

class Solution745:
    pass
