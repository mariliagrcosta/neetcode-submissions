class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        text_length = len(s2)
        window_size = len(s1)

        if window_size > text_length:
            return False

        for start in range(text_length - window_size + 1):
            target_count = [0] * 26
            window_count = [0] * 26

            for offset in range(window_size):
                target_count[ord(s1[offset]) - ord("a")] += 1
                window_count[ord(s2[start + offset]) - ord("a")] += 1

            if target_count == window_count:
                return True

        return False
