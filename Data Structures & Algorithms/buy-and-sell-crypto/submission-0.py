class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            price = prices[i]

            if price < lowest_price:
                lowest_price = price
            else:
                profit = price - lowest_price
                max_profit = max(max_profit, profit)

        return max_profit
