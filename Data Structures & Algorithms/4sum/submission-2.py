class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.k_sum(nums, target, k=4, start=0)

    def k_sum(self, nums: list[int], target: int, k: int, start: int) -> list[list[int]]:
        results = []
        n = len(nums)

        if start >= n:
            return results

        if k == 2:
            left = start
            right = n - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    results.append([nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

            return results

        for i in range(start, n - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue

            min_sum = nums[i] + sum(nums[i + 1:i + k])
            max_sum = nums[i] + sum(nums[-(k - 1):])
            
            if min_sum > target:
                break

            if max_sum < target:
                continue

            for subset in self.k_sum(nums, target - nums[i], k - 1, i + 1):
                results.append([nums[i]] + subset)

        return results
