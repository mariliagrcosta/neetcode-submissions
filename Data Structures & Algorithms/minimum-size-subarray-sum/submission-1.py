from bisect import bisect_left


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = [0]

        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        n = len(nums)
        min_length = float("inf")

        for start in range(n):
            required_sum = prefix_sum[start] + target

            end = bisect_left(prefix_sum, required_sum)

            if end <= n:
                min_length = min(min_length, end - start)

        if min_length == float("inf"):
            return 0

        return min_length
