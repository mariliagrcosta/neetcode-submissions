class StockSpanner:
    def __init__(self):
        self.daily_prices = []
        self.candidate_days = []  # Prices at these days strictly decrease

    def next(self, price: int) -> int:
        current_day = len(self.daily_prices)
        self.daily_prices.append(price)

        while (
            self.candidate_days
            and self.daily_prices[self.candidate_days[-1]] <= price
        ):
            self.candidate_days.pop()

        if self.candidate_days:
            previous_greater_day = self.candidate_days[-1]
        else:
            previous_greater_day = -1

        current_span = current_day - previous_greater_day
        self.candidate_days.append(current_day)

        return current_span
