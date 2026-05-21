class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                for j in range(i, length - 1):
                    nums[j] = nums[j + 1]
                length -= 1
            else:
                i += 1
        return length