class FreqStack:
    def __init__(self):
        self.value_frequencies = defaultdict(int)
        self.frequency_stacks = defaultdict(list)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.value_frequencies[val] += 1

        current_frequency = self.value_frequencies[val]
        self.frequency_stacks[current_frequency].append(val)

        self.max_frequency = max(self.max_frequency, current_frequency)

    def pop(self) -> int:
        most_frequent_value = self.frequency_stacks[self.max_frequency].pop()
        self.value_frequencies[most_frequent_value] -= 1

        if not self.frequency_stacks[self.max_frequency]:
            self.max_frequency -= 1

        return most_frequent_value
