class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # right is exclusive

        while left < right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        return -1
