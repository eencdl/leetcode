__author__ = 'don'
"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        if 2*k >= len(prices):
            return self.maxProfitAnyK(prices)
        return self.maxProfitK(k, prices)

    def maxProfitK(self, k, prices):
        n = len(prices)
        dp = [None] * n #None is less than most -ve
        dp[0] = 0
        for i in range(n):
            print '-----------'
            # range 1, i+1, +1 are all offset since dp[0] is starting,
            # and i is 0
            for j in range(1, min(2*k, i+1) + 1):
                # [1,2][x] , x is index to the preceding array [1,2]
                # buyProfit is the maximum profit and the last action is buy
                # sellProfit is the maximum profit and the last action is sell
                # j is Odd, buyProfit[j] = max(buyProfit[j], sellProfit[j-1] - prices[i]) , is it worth buying
                # j is Even, sellProfit[j] = max(sellProfit[j], buyProfit[j-1] + prices[i]), is it worth selling
                # this algorithm show a transaction can be 0, i.e. prices[i] - prices[i]
                # bear in mind the final result, j is always even because a transaction is a pair
                dp[j] = max(dp[j], dp[j-1] + prices[i] * [1, -1][j%2])
        return dp[2*k]



    def maxProfitAnyK(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit

if __name__ == '__main__':
    print Solution().maxProfit(2,[1, 2, 4, 2, 5, 7, 2, 4, 9, 0])

