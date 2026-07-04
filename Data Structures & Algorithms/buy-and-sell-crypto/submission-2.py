class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        buy = prices[0]
        for i in range(1, n):
            sell = prices[i]
            profit = sell - buy
            max_profit = max(max_profit, profit)
            buy = min(buy, prices[i])

        return max_profit