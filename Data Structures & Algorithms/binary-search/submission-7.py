class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # right is exclusive

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > target:
                right = middle
            else:
                left = middle + 1

        if left > 0 and nums[left - 1] == target:
            return left - 1

        return -1
