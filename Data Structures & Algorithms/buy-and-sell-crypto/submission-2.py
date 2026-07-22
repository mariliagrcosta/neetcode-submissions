class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for buy_day in range(len(prices)):
            for sell_day in range(buy_day + 1, len(prices)):
                profit = prices[sell_day] - prices[buy_day]

                if profit > max_profit:
                    max_profit = profit

        return max_profit
