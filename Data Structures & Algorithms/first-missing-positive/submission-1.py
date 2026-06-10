class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            value = abs(nums[i])
            if value <= n:
                mark_idx = value - 1
                if nums[mark_idx] > 0:
                    nums[mark_idx] = -nums[mark_idx]

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
