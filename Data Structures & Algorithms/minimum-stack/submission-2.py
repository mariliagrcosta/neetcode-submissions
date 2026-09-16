class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum_value = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minimum_value = val
        else:
            difference = val - self.minimum_value
            self.stack.append(difference)

            if difference < 0:
                self.minimum_value = val

    def pop(self) -> None:
        difference = self.stack.pop()

        if difference < 0:
            self.minimum_value = self.minimum_value - difference

    def top(self) -> int:
        difference = self.stack[-1]

        if difference < 0:
            return self.minimum_value

        return self.minimum_value + difference

    def getMin(self) -> int:
        return self.minimum_value
