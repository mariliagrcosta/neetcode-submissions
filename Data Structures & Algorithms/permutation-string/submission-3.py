class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        text_length = len(s2)
        window_size = len(s1)

        if window_size > text_length:
            return False

        sorted_target = sorted(s1)

        for start in range(text_length - window_size + 1):
            sorted_window = sorted(s2[start:start + window_size])

            if sorted_target == sorted_window:
                return True

        return False
