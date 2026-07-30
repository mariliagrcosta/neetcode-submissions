class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        unique_chars = set(s)
        max_length = 0

        for target_char in unique_chars:
            target_count = left = 0

            for right in range(len(s)):
                if s[right] == target_char:
                    target_count += 1

                while (right - left + 1) - target_count > k:
                    if s[left] == target_char:
                        target_count -= 1

                    left += 1

                max_length = max(max_length, right - left + 1)

        return max_length
