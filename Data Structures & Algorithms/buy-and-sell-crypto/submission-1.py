class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_profit = 0

        for i in range(1, len(prices)):
            daily_change = prices[i] - prices[i - 1]
            new_profit = current_profit + daily_change

            if new_profit > 0:
                current_profit = new_profit

                if current_profit > max_profit:
                    max_profit = current_profit
            else:
                current_profit = 0

        return max_profit
