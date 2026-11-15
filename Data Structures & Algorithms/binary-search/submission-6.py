class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def lower_bound(left: int, right: int) -> int:
            if left >= right:
                return left

            middle = (left + right) // 2

            if nums[middle] < target:
                return lower_bound(middle + 1, right)
            else:
                return lower_bound(left, middle)

        index = lower_bound(0, len(nums))  # right is exclusive

        if index < len(nums) and nums[index] == target:
            return index

        return -1
