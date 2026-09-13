class MyQueue:
    def __init__(self) -> None:
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        top_value = self.stack.pop()

        if not self.stack:
            return top_value

        front_value = self.pop()
        self.stack.append(top_value)

        return front_value

    def peek(self) -> int:
        top_value = self.stack.pop()

        if not self.stack:
            self.stack.append(top_value)
            return top_value

        front_value = self.peek()
        self.stack.append(top_value)

        return front_value

    def empty(self) -> bool:
        return not self.stack
