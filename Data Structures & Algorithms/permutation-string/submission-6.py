class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        text_length = len(s2)

        if window_size > text_length:
            return False

        window_count = [0] * 26
        target_count = [0] * 26

        for i in range(window_size):
            target_count[ord(s1[i]) - ord("a")] += 1
            window_count[ord(s2[i]) - ord("a")] += 1

        matches = 0

        for i in range(26):
            if target_count[i] == window_count[i]:
                matches += 1

        left = 0

        for right in range(window_size, text_length):
            if matches == 26:
                return True

            index = ord(s2[right]) - ord("a")
            window_count[index] += 1

            if target_count[index] == window_count[index]:
                matches += 1
            elif target_count[index] + 1 == window_count[index]:
                matches -= 1

            index = ord(s2[left]) - ord("a")
            window_count[index] -= 1

            if target_count[index] == window_count[index]:
                matches += 1
            elif target_count[index] - 1 == window_count[index]:
                matches -= 1

            left += 1

        return matches == 26
