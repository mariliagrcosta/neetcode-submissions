class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = set()
        n = len(nums)
        nums.sort()

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                seen = set()
                required_sum = target - (nums[i] + nums[j])

                for k in range(j + 1, n):
                    complement = required_sum - nums[k]

                    if complement in seen:
                        quadruplets.add((nums[i], nums[j], complement, nums[k]))

                    seen.add(nums[k])

        return [list(quad) for quad in quadruplets]
