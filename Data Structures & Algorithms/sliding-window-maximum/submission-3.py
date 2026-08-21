from sortedcontainers import SortedList


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_maxima = []
        window_values = SortedList()

        for right, num in enumerate(nums):
            window_values.add(num)

            left = right - k + 1

            if left > 0:
                window_values.remove(nums[left - 1])

            if left >= 0:
                window_maxima.append(window_values[-1])

        return window_maxima
