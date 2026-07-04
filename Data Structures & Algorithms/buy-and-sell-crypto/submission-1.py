class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        buy = 0
        for i in range(n):
            if i == 0:
                buy = prices[i]
                continue
            sell = prices[i]
            profit = sell - buy
            max_profit = max(max_profit, profit)
            buy = min(buy, prices[i])

        return max_profit