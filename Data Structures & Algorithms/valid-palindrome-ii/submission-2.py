class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_window(left, right, skipped):
            while left < right:
                if s[left] != s[right]:
                    if skipped:
                        return False
                    
                    return (
                        check_window(left + 1, right, True)
                        or check_window(left, right - 1, True)
                    )

                left += 1
                right -= 1

            return True

        return check_window(0, len(s) - 1, False)
