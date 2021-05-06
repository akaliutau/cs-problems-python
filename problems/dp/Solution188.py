"""   
   DP
   
   
   The value of balance[d][t][s] represents the best profit (i.e. balance) we can have at the end of
   the d-th day, with t remaining transactions to make and s stocks.
   
   The next step is finding out the so-called "transition equation", which is a
   method that tells you how to jump from one state to another.
   
   We start with balance[0][0][0] = 0 and balance[0][0][1]=-prices[0], and our final aim
   is max of balance[n-1][t][0] from t=0 to t=k. Now, we need to fill out the entire
   array to find out the result. Assume we have gotten the results before day d,
   and we need to calculate the profit of day d. There are only four possible
   actions we can do on day d: 
   
   1. keep holding the stock, 
   2. keep not holding the stock, 
   3. buy the stock, or 
   4. sell the stock. 
   
   The profit is easy to calculate.
   
   Keep holding the stock: balance[d][t][1] = balance[d-1][t][1]
   
   Keep not holding the stock: balance[d][t][0] = balance[d-1][t][0]
   
   Buying, when t > 0: balance[d][t][1] = balance[d-1][t-1][0] - prices[d]
   
   Selling: balance[d][t][0] = balance[d-1][t][1] + prices[d]
   
   We can combine they together to find the maximum profit:
   
   balance[d][t][1] = max(balance[d-1][t][1], balance[d-1][t-1][0] - prices[d]) // update for "hold" stock scenario
   balance[d][t][0] = max(balance[d-1][t][0], balance[d-1][t][1] + prices[d])   // update for "not hold" stock scenario
   
   
"""

class Solution188:
    pass
