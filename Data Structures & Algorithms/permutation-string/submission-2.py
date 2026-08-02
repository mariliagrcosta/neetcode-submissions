from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        text_length = len(s2)
        window_size = len(s1)

        if window_size > text_length:
            return False

        target_count = Counter(s1)
        window_count = Counter(s2[:window_size])

        if target_count == window_count:
            return True

        left = 0

        for right in range(window_size, text_length):
            char_in = s2[right]
            char_out = s2[left]

            window_count[char_in] += 1
            window_count[char_out] -= 1

            if window_count[char_out] == 0:
                del window_count[char_out]

            left += 1

            if target_count == window_count:
                return True

        return False
