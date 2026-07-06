class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        rotated_array = [0] * n

        for i in range(n):
            rotated_array[(i + k) % n] = nums[i]

        nums[:] = rotated_array
