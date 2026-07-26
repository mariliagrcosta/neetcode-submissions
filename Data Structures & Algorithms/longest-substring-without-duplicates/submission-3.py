class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0

        for left in range(len(s)):
            seen = set()

            for right in range(left, n):
                if s[right] in seen:
                    break

                seen.add(s[right])
                max_length = max(max_length, right - left + 1)

        return max_length
