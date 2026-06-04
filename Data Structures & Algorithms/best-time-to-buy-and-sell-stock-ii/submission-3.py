class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash, hold = 0, -prices[0]

        for price in prices[1:]:
            next_hold = max(hold, cash - price)
            next_cash = max(cash, hold + price)

            hold = next_hold
            cash = next_cash

        return cash
