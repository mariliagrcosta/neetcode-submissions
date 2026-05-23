class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        for n in nums:
            elements[n] = elements.get(n, 0) + 1
        return max(elements, key=elements.get)