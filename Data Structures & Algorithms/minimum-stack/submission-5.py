class Node:
    def __init__(self, val: int, minimum_value: int, next_node=None):
        self.value = val
        self.minimum_value = minimum_value
        self.next = next_node


class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, val)
        else:
            current_minimum = min(val, self.head.minimum_value)
            self.head = Node(val, current_minimum, self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.value

    def getMin(self) -> int:
        return self.head.minimum_value
