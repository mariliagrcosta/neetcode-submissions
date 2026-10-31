import heapq
from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.value_frequencies = defaultdict(int)
        self.max_heap = []
        self.insertion_index = 0

    def push(self, val: int) -> None:
        self.value_frequencies[val] += 1
        self.insertion_index += 1

        # heapq is a min-heap, so negate the priority keys to simulate a max-heap
        heapq.heappush(
            self.max_heap,
            (-self.value_frequencies[val], -self.insertion_index, val),
        )

    def pop(self) -> int:
        # Ignore negated priority keys (-frequency, -insertion_index)
        _, _, most_frequent_value = heapq.heappop(self.max_heap)
        self.value_frequencies[most_frequent_value] -= 1

        return most_frequent_value
