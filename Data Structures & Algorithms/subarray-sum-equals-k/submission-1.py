class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)

        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        count = 0

        for start in range(n):
            for end in range(start + 1, n + 1):
                if prefix_sums[end] - prefix_sums[start] == k:
                    count += 1

        return count
