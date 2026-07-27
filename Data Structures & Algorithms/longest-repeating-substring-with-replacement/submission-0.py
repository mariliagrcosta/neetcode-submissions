class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            max_frequency = max(max_frequency, frequency[s[right]])

            while (right - left + 1) - max_frequency > k:
                frequency[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length