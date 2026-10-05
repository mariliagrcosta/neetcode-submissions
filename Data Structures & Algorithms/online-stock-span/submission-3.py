class StockSpanner:
    def __init__(self):
        self.daily_prices = []
        self.daily_spans = []

    def next(self, price: int) -> int:
        current_span = 1
        candidate_day = len(self.daily_prices) - 1

        while (
            candidate_day >= 0
            and self.daily_prices[candidate_day] <= price
        ):
            candidate_span = self.daily_spans[candidate_day]
            current_span += candidate_span
            candidate_day -= candidate_span

        self.daily_prices.append(price)
        self.daily_spans.append(current_span)

        return current_span
