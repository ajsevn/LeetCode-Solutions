class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        for i in range(1, len(prices)):
            # If the current price is greater than the previous price,
            # we can sell the stock at the current price and make a profit.
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit
