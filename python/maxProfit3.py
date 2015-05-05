__author__ = 'don'
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    """
    Comparing to I and II, III limits the number of transactions to 2.
    This can be solve by "devide and conquer".
    We use left[i] to track the maximum profit for transactions before i,
    and use right[i] to track the maximum profit for transactions after i.
    You can use the following example to understand the Java solution:

    Prices: 1 4 5 7 6 3 2 9
    left = [0, 3, 4, 6, 6, 6, 6, 8]
    right= [8, 7, 7, 7, 7, 7, 7, 0]
    The maximum profit = 13
    """
    def maxProfit3(self,prices):
        l = len(prices)
        if l < 2:
            return 0

        left = [0 for i in range(l)]
        right = [0 for i in range(l)]
        ma = prices[-1]
        mi = prices[0]
        for i in range(1, l):
            left[i] = max(left[i-1], prices[i]-mi)
            mi = min(mi, prices[i])
            right[-i-1] = max(right[-i], ma - prices[-i-1])
            ma = max(ma, prices[-i-1])

        profit = 0
        for i in range(l):
            profit = max(left[i] + right[i], profit)

        return profit