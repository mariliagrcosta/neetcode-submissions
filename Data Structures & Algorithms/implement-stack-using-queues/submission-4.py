class MyStack:
    def __init__(self):
        self.queue = None

    def push(self, x: int) -> None:
        self.queue = deque([x, self.queue])

    def pop(self) -> int:
        top_element = self.queue.popleft()
        self.queue = self.queue.popleft()

        return top_element

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
