class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        text_length = len(s2)
        window_size = len(s1)

        if window_size > text_length:
            return False

        target_count = [0] * 26
        window_count = [0] * 26

        for i in range(window_size):
            target_count[ord(s1[i]) - ord("a")] += 1
            window_count[ord(s2[i]) - ord("a")] += 1

        if target_count == window_count:
            return True

        left = 0

        for right in range(window_size, text_length):
            window_count[ord(s2[right]) - ord("a")] += 1
            window_count[ord(s2[left]) - ord("a")] -= 1
            left += 1

            if target_count == window_count:
                return True

        return False
