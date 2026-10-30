from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.value_frequencies = defaultdict(int)
        self.frequency_stacks = []

    def push(self, val: int) -> None:
        self.value_frequencies[val] += 1
        current_frequency = self.value_frequencies[val]

        if current_frequency > len(self.frequency_stacks):
            self.frequency_stacks.append([])

        self.frequency_stacks[current_frequency - 1].append(val)

    def pop(self) -> int:
        highest_stack = self.frequency_stacks[-1]
        most_frequent_value = highest_stack.pop()
        self.value_frequencies[most_frequent_value] -= 1

        if not highest_stack:
            self.frequency_stacks.pop()

        return most_frequent_value
