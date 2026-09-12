class MyQueue:
    def __init__(self) -> None:
        self.main_stack = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        self._transfer_to_helper()
        value = self.helper_stack.pop()
        self._restore_to_main()

        return value

    def peek(self) -> int:
        self._transfer_to_helper()
        value = self.helper_stack[-1]
        self._restore_to_main()

        return value

    def empty(self) -> bool:
        return not self.main_stack

    def _transfer_to_helper(self) -> None:
        while self.main_stack:
            self.helper_stack.append(self.main_stack.pop())

    def _restore_to_main(self) -> None:
        while self.helper_stack:
            self.main_stack.append(self.helper_stack.pop())
