class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        min_data = prices[0]
        profit = 0
        for price in prices:
            profit = max(profit, price-min_data)
            min_data = min(min_data, price)
        return profit

        