class MinStack:
    def __init__(self):
        self.value_stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        self.value_stack.append(val)

        if not self.minimum_stack:
            current_minimum = val
        else:
            current_minimum = min(val, self.minimum_stack[-1])

        self.minimum_stack.append(current_minimum)

    def pop(self) -> None:
        self.value_stack.pop()
        self.minimum_stack.pop()

    def top(self) -> int:
        return self.value_stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]
