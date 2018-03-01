"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0

        maxprofit = 0
        minprice = prices[0]
        for i in range(len(prices)):
            if prices[i] > minprice:
                maxprofit = max(maxprofit, prices[i] - minprice)
            else:
                minprice = prices[i]
        return maxprofit

if __name__ == '__main__':
    sol = Solution()
    assert (sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
    assert (sol.maxProfit([]) == 0)
    assert (sol.maxProfit([1, 4, 2]) == 3)