class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left >= right:
                return -1

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return binary_search(middle + 1, right)
            else:
                return binary_search(left, middle)

        return binary_search(0, len(nums))  # right is exclusive
