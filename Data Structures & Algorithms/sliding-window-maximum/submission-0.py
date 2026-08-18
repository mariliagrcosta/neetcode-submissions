class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_maxima = []
        candidate_indices = deque()

        for right, num in enumerate(nums):
            left = right - k + 1

            if candidate_indices and candidate_indices[0] < left:
                candidate_indices.popleft()

            while candidate_indices and nums[candidate_indices[-1]] < num:
                candidate_indices.pop()

            candidate_indices.append(right)

            if left >= 0:
                window_maxima.append(nums[candidate_indices[0]])

        return window_maxima
