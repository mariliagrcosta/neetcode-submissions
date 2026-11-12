from bisect import bisect_left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index

        return -1
