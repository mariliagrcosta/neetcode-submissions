class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def calculate_profit(day: int, holding_stock: bool) -> int:
            if day >= len(prices):
                return 0

            skip = calculate_profit(day + 1, holding_stock)

            if holding_stock:
                sell = prices[day] + calculate_profit(day + 1, False)
                return max(skip, sell)
            else:
                buy = -prices[day] + calculate_profit(day + 1, True)
                return max(skip, buy)

        return calculate_profit(0, False)
      
