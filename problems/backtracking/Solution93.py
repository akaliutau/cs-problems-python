"""   Given a string s containing only digits, return all possible valid IP
   addresses that can be obtained from s. You can return them in any order.
   
   A valid IP address consists of exactly four integers, each integer is between
   0 and 255, separated by single dots and cannot have leading zeros. For
   example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and
   "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
   
   
   
   Example 1:
   
   Input: s = "25525511135" Output: ["255.255.11.135","255.255.111.35"]
   
   IDEA:
   1) try to cut a block from 1 to 3 symbols in length, check its validness, and if all is okay, go to step #2
   2) repeat until have non-empty input
   
"""

class Solution93:
    pass
