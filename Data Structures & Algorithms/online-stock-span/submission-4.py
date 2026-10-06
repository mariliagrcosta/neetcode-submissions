class StockSpanner:
    def __init__(self):
        self.daily_prices = []

    def next(self, price: int) -> int:
        self.daily_prices.append(price)
        current_day = len(self.daily_prices) - 1
        previous_day = current_day - 1

        while (
            previous_day >= 0
            and self.daily_prices[previous_day] <= price
        ):
            previous_day -= 1

        return current_day - previous_day
