class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low < high:
            middle = (low + high) // 2
            guess_result = guess(middle)

            if guess_result <= 0:
                high = middle
            else:
                low = middle + 1

        return low
