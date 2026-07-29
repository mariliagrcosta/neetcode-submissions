class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        max_length = 0

        for left in range(len(s)):
            frequency = [0] * 26
            max_frequency = 0

            for right in range(left, len(s)):
                char_index = ord(s[right]) - ord("A")
                frequency[char_index] += 1
                max_frequency = max(max_frequency, frequency[char_index])

                window_size = right - left + 1
                if window_size - max_frequency <= k:
                    max_length = max(max_length, window_size)

        return max_length
