from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.value_frequencies = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.value_frequencies[val] += 1

    def pop(self) -> int:
        max_frequency = max(self.value_frequencies.values())

        for index in range(len(self.stack) - 1, -1, -1):
            value = self.stack[index]

            if self.value_frequencies[value] == max_frequency:
                self.value_frequencies[value] -= 1

                return self.stack.pop(index)
