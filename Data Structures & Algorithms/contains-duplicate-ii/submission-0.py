class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for current_index, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)
            if len(window) > k:
                window.remove(nums[current_index - k])

        return False
