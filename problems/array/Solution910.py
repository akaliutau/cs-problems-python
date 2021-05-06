"""   Given an array A of integers, for each integer A[i] we need to choose either
   x = -K or x = K, and add x to A[i] (only once). After this process, we have
   some array B. Return the smallest possible difference between the maximum
   value of B and the minimum value of B. 
   
   IDEA: if A[i] < A[j], we don't need to
   consider when A[i] goes down while A[j] goes up. This is because the interval
   (A[i] + K, A[j] - K) is inside the interval (A[i] - K, A[j] + K) (here, (a, b) for a > b denotes (b, a) instead.) 
   
   In other words, for A[i] < A[j] (sorted array) the interval
   (A[i] + K, A[j] - K) is more narrow than this one : (A[i] - K, A[j] + K)
   
   
   So the best strategy on every element of array will be:
   1) add k to the left elem
   2) sub k from the right elem
   
   For sorted A, say A[i] is the largest i that goes up. 
   Then A[0] + K, ... , A[i] + K, A[i+1] - K, ... ,  A[A.length - 1] - K 
   are the only relevant values for calculating the answer: every other value is between one of these
   extremal values. 
   
   
   
   Example 1: Input: A = [1], K = 0 Output: 0 Explanation: B =
   [1]
"""

class Solution910:
    pass
