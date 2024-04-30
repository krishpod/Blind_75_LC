'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Hint : find local min and search for local max, sliding window
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        track = prices[0]

        for i in range(1, len(prices)):
            profit = max(prices[i]-track, profit)
            track = min(track, prices[i])
        return profit

a = Solution()
b = Solution()
print(a.maxProfit([7,1,5,3,6,4]))
print(b.maxProfit([7,6,4,3,1]))

