class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = [0] * 26
        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            char_index = ord(s[right]) - ord("A")
            frequency[char_index] += 1
            max_frequency = max(max_frequency, frequency[char_index])

            while (right - left + 1) - max_frequency > k:
                char_index = ord(s[left]) - ord("A")
                frequency[char_index] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length