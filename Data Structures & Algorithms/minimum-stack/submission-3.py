class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum_value = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minimum_value = val
        elif val < self.minimum_value:
            encoded_value = 2 * val - self.minimum_value
            self.stack.append(encoded_value)
            self.minimum_value = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        popped_value = self.stack.pop()

        if popped_value < self.minimum_value:
            self.minimum_value = 2 * self.minimum_value - popped_value

    def top(self) -> int:
        top_value = self.stack[-1]

        if top_value < self.minimum_value:
            return self.minimum_value

        return top_value

    def getMin(self) -> int:
        return self.minimum_value
