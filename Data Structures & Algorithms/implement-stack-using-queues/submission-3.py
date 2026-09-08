class MyStack:
    def __init__(self):
        self.primary_queue = deque()
        self.helper_queue = deque()

    def push(self, x: int) -> None:
        self.primary_queue.append(x)

    def pop(self) -> int:
        while len(self.primary_queue) > 1:
            self.helper_queue.append(self.primary_queue.popleft())

        top_element = self.primary_queue.popleft()

        self.primary_queue, self.helper_queue = self.helper_queue, self.primary_queue

        return top_element

    def top(self) -> int:
        while len(self.primary_queue) > 1:
            self.helper_queue.append(self.primary_queue.popleft())

        top_element = self.primary_queue.popleft()
        self.helper_queue.append(top_element)

        self.primary_queue, self.helper_queue = self.helper_queue, self.primary_queue

        return top_element

    def empty(self) -> bool:
        return not self.primary_queue
