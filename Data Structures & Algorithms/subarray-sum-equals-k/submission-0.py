class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        for start in range(len(nums)):
            subarray_sum = 0
            for end in range(start, len(nums)):
                subarray_sum += nums[end]
                if subarray_sum == k:
                    count += 1

        return count
