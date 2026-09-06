class MyStack:
    def __init__(self):
        self.primary_queue = deque()
        self.helper_queue = deque()

    def push(self, x: int) -> None:
        self.helper_queue.append(x)

        while self.primary_queue:
            self.helper_queue.append(self.primary_queue.popleft())

        self.primary_queue, self.helper_queue = self.helper_queue, self.primary_queue

    def pop(self) -> int:
        return self.primary_queue.popleft()

    def top(self) -> int:
        return self.primary_queue[0]

    def empty(self) -> bool:
        return not self.primary_queue
