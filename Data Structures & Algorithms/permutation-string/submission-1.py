class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        text_length = len(s2)
        window_size = len(s1)

        if window_size > text_length:
            return False

        target_count = {}
        window_count = {}

        for i in range(window_size):
            target_count[s1[i]] = target_count.get(s1[i], 0) + 1
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

        if target_count == window_count:
            return True

        left = 0

        for right in range(window_size, text_length):
            char_in = s2[right]
            char_out = s2[left]

            window_count[char_in] = window_count.get(char_in, 0) + 1
            window_count[char_out] -= 1

            if window_count[char_out] == 0:
                del window_count[char_out]

            left += 1

            if target_count == window_count:
                return True

        return False
