class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = set()
        for x in nums:
            if x in checked:
                return True
            checked.add(x)
        return False
