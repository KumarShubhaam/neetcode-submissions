class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        future_sell = [0] * n
        # find the future sell price
        temp = 0
        for i in range(n-1, -1, -1):
            temp = max(prices[i], temp)
            future_sell[i] = temp
        # print(future_sell)

        max_profit = 0
        for i, p in enumerate(prices):
            profit = future_sell[i] - p
            max_profit = max(profit, max_profit)

        return max_profit
