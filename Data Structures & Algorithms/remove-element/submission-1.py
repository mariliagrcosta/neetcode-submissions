class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        available_position = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[available_position] = nums[i]
                available_position += 1
        return available_position