class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3
        for num in nums:
            count[num] += 1

        index = 0
        for color, frequency in enumerate(count):
            for _ in range(frequency):
                nums[index] = color
                index += 1
