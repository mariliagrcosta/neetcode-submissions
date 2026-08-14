class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target_counts = {}
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1

        window_counts = {}
        satisfied_chars = 0
        required_chars = len(target_counts)

        left = 0
        min_length = float("inf")
        min_start = 0

        for right in range(len(s)):
            right_char = s[right]

            if right_char in target_counts:
                window_counts[right_char] = window_counts.get(right_char, 0) + 1

                if window_counts[right_char] == target_counts[right_char]:
                    satisfied_chars += 1

            while satisfied_chars == required_chars:
                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    min_start = left

                left_char = s[left]

                if left_char in target_counts:
                    window_counts[left_char] -= 1

                    if window_counts[left_char] < target_counts[left_char]:
                        satisfied_chars -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_start:min_start + min_length]
