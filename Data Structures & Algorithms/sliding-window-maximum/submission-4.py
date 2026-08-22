class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        segment_tree = [float("-inf")] * (2 * length)

        for index in range(length):
            segment_tree[length + index] = nums[index]

        for index in range(length - 1, 0, -1):
            segment_tree[index] = max(
                segment_tree[2 * index], segment_tree[2 * index + 1]
            )

        def query_max(left: int, right: int) -> int:
            left += length
            right += length + 1
            result = float("-inf")

            while left < right:
                if left % 2 == 1:
                    result = max(result, segment_tree[left])
                    left += 1

                if right % 2 == 1:
                    right -= 1
                    result = max(result, segment_tree[right])

                left //= 2
                right //= 2

            return result

        window_maxima = []

        for index in range(length - k + 1):
            window_maxima.append(query_max(index, index + k - 1))

        return window_maxima
