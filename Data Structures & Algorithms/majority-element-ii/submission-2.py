class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_votes = {}

        for num in nums:
            candidate_votes[num] = candidate_votes.get(num, 0) + 1

            if len(candidate_votes) <= 2:
                continue

            candidate_votes = {
                candidate: votes - 1 
                for candidate, votes in candidate_votes.items() 
                if votes > 1
            }

        majority_elements = []
        threshold = len(nums) // 3

        for candidate in candidate_votes:
            if nums.count(candidate) > threshold:
                majority_elements.append(candidate)

        return majority_elements
