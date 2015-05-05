__author__ = 'don'
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
"""
class Solution:
    def maxProfit1(self, prices):
        #keep track of the most minimum
        #take the most positive and subtract
        if len(prices) < 2:
             return 0

        m = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - m)
            m = min(m , prices[i])

        return profit