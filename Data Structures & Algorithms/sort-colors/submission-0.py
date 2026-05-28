class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = {0: 0, 1: 0, 2: 0}
        for num in nums:
            count[num] += 1

        index = 0
        for color, frequency in count.items():
            for _ in range(frequency):
                nums[index] = color
                index += 1
