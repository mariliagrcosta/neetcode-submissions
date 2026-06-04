class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def calculate_profit(day: int, holding_stock: bool) -> int:
            if day >= len(prices):
                return 0

            state = (day, holding_stock)
            if state in memo:
                return memo[state]

            skip = calculate_profit(day + 1, holding_stock)

            if holding_stock:
                sell = prices[day] + calculate_profit(day + 1, False)
                memo[state] = max(skip, sell)
            else:
                buy = -prices[day] + calculate_profit(day + 1, True)
                memo[state] = max(skip, buy)

            return memo[state]

        return calculate_profit(0, False)
