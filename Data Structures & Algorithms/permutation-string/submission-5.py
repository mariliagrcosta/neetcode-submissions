class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        text_length = len(s2)

        if window_size > text_length:
            return False

        target_count = {}

        for char in s1:
            target_count[char] = target_count.get(char, 0) + 1

        required_matches = len(target_count)

        for start in range(text_length):
            window_count = {}
            current_matches = 0

            for end in range(start, text_length):
                char = s2[end]
                window_count[char] = window_count.get(char, 0) + 1
                required_count = target_count.get(char, 0)

                if required_count < window_count[char]:
                    break

                if required_count == window_count[char]:
                    current_matches += 1

                if current_matches == required_matches:
                    return True

        return False
