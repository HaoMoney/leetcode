class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0
        max_profit = [0] * len(prices)
        for i in range(1,len(max_profit)):
            max_profit[i] = max(max_profit[i-1],prices[i]-min(prices[:i]))
        return max_profit[-1]
