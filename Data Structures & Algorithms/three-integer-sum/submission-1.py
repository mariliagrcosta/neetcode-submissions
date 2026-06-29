class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()
            j = i + 1

            while j < len(nums):
                complement = -(nums[i] + nums[j])

                if complement in seen:
                    triplets.add((nums[i], complement, nums[j]))

                seen.add(nums[j])
                j += 1

        return [list(t) for t in triplets]
