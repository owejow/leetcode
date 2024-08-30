class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            prev = prices[i - 1]
            cur = prices[i]
            if prev < cur:
                profit += cur - prev
        return profit
