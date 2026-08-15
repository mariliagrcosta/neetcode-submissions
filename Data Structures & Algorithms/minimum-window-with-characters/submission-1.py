class Solution:
    @staticmethod
    def get_index(char):
        if char.isupper():
            return ord(char) - ord("A")

        return ord(char) - ord("a") + 26

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target_counts = [0] * 52

        for char in t:
            index = self.get_index(char)
            target_counts[index] += 1

        window_counts = [0] * 52
        satisfied_chars = 0
        required_chars = 0

        for count in target_counts:
            if count > 0:
                required_chars += 1

        left = 0
        min_length = float("inf")
        min_start = 0

        for right in range(len(s)):
            right_char = s[right]
            right_index = self.get_index(right_char)

            if target_counts[right_index] > 0:
                window_counts[right_index] += 1

                if window_counts[right_index] == target_counts[right_index]:
                    satisfied_chars += 1

            while satisfied_chars == required_chars:
                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    min_start = left

                left_char = s[left]
                left_index = self.get_index(left_char)

                if target_counts[left_index] > 0:
                    window_counts[left_index] -= 1

                    if window_counts[left_index] < target_counts[left_index]:
                        satisfied_chars -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_start : min_start + min_length]
