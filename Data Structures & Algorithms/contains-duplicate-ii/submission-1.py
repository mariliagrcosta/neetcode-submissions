class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for current_index, num in enumerate(nums):
            if num in last_seen and current_index - last_seen[num] <= k:
                return True

            last_seen[num] = current_index

        return False
