class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n + 1  # high is exclusive

        while low < high:
            middle = (low + high) // 2
            guess_result = guess(middle)

            if guess_result == 0:
                return middle
            elif guess_result == -1:
                high = middle
            else:
                low = middle + 1
