class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target_counts = Counter(t)
        required_chars = len(target_counts)

        filtered_s = [
            (index, char)
            for index, char in enumerate(s)
            if char in target_counts
        ]

        window_counts = Counter()
        satisfied_chars = 0

        left = 0
        min_length = float("inf")
        min_start = 0

        for right in range(len(filtered_s)):
            right_index, right_char = filtered_s[right]
            window_counts[right_char] += 1

            if window_counts[right_char] == target_counts[right_char]:
                satisfied_chars += 1

            while satisfied_chars == required_chars:
                left_index, left_char = filtered_s[left]
                window_length = right_index - left_index + 1

                if window_length < min_length:
                    min_length = window_length
                    min_start = left_index

                window_counts[left_char] -= 1

                if window_counts[left_char] < target_counts[left_char]:
                    satisfied_chars -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_start : min_start + min_length]
