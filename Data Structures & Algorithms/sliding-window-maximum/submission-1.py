class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        left_max = [0] * length
        right_max = [0] * length

        for index in range(length):
            if index % k == 0:
                left_max[index] = nums[index]
            else:
                left_max[index] = max(left_max[index - 1], nums[index])

        for index in range(length - 1, -1, -1):
            if (index + 1) % k == 0 or index == length - 1:
                right_max[index] = nums[index]
            else:
                right_max[index] = max(right_max[index + 1], nums[index])

        window_maxima = []

        for left in range(length - k + 1):
            right = left + k - 1
            window_maximum = max(right_max[left], left_max[right])
            window_maxima.append(window_maximum)

        return window_maxima
