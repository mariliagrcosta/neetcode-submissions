class StockSpanner:
    def __init__(self):
        self.price_days = []
        self.day_count = 0

    def next(self, price: int) -> int:
        while self.price_days and self.price_days[-1][0] <= price:
            self.price_days.pop()

        if self.price_days:
            _, previous_greater_day = self.price_days[-1]
        else:
            previous_greater_day = -1

        current_span = self.day_count - previous_greater_day

        self.price_days.append((price, self.day_count))
        self.day_count += 1

        return current_span
