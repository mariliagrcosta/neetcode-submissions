class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_a, candidate_b = None, None
        votes_a, votes_b = 0, 0

        for num in nums:
            if num == candidate_a:
                votes_a += 1
            elif num == candidate_b:
                votes_b += 1
            elif votes_a == 0:
                candidate_a, votes_a = num, 1
            elif votes_b == 0:
                candidate_b, votes_b = num, 1
            else:
                votes_a -= 1
                votes_b -= 1

        votes_a, votes_b = 0, 0

        for num in nums:
            if num == candidate_a:
                votes_a += 1
            elif num == candidate_b:
                votes_b += 1

        majority_elements = []
        threshold = len(nums) // 3

        if votes_a > threshold:
            majority_elements.append(candidate_a)
        if votes_b > threshold:
            majority_elements.append(candidate_b)

        return majority_elements
