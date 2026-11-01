from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.value_frequencies = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.value_frequencies[val] += 1

    def pop(self) -> int:
        most_frequent_value = None
        highest_frequency = 0
        most_recent_index = -1

        for index in range(len(self.stack) - 1, -1, -1):
            value = self.stack[index]
            frequency = self.value_frequencies[value]

            if frequency > highest_frequency:
                most_frequent_value = value
                highest_frequency = frequency
                most_recent_index = index

        self.stack.pop(most_recent_index)
        self.value_frequencies[most_frequent_value] -= 1

        return most_frequent_value
