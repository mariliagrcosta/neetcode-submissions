class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        NOT_HOLD, HOLD = 0, 1

        profit_table = [[0, 0] for _ in range(n)]
        profit_table[0][NOT_HOLD] = 0
        profit_table[0][HOLD] = -prices[0]

        for i in range(1, n):
            profit_table[i][HOLD] = max(
                profit_table[i-1][HOLD], 
                profit_table[i-1][NOT_HOLD] - prices[i]
            )
            profit_table[i][NOT_HOLD] = max(
                profit_table[i-1][NOT_HOLD], 
                profit_table[i-1][HOLD] + prices[i]
            )

        return profit_table[n - 1][NOT_HOLD]
