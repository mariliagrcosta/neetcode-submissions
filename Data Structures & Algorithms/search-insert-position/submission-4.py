class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        insert_position = 0
        jump_size = 1 << (len(nums).bit_length() - 1)

        while jump_size:
            if (
                insert_position + jump_size <= len(nums)
                and nums[insert_position + jump_size - 1] < target
            ):
                insert_position += jump_size

            jump_size //= 2

        return insert_position
