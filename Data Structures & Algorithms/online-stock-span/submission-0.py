class StockSpanner:
    def __init__(self):
        self.price_spans = []

    def next(self, price: int) -> int:
        current_span = 1

        while self.price_spans and self.price_spans[-1][0] <= price:
            _, absorbed_span = self.price_spans.pop()
            current_span += absorbed_span

        self.price_spans.append((price, current_span))

        return current_span
