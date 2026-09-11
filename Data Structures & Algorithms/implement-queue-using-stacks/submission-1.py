class MyQueue:
    def __init__(self) -> None:
        self.main_stack = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        while self.main_stack:
            self.helper_stack.append(self.main_stack.pop())

        self.main_stack.append(x)

        while self.helper_stack:
            self.main_stack.append(self.helper_stack.pop())

    def pop(self) -> int:
        return self.main_stack.pop()

    def peek(self) -> int:
        return self.main_stack[-1]

    def empty(self) -> bool:
        return not self.main_stack
