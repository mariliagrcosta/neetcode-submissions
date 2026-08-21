class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_maxima = []
        max_heap = []

        for right, num in enumerate(nums):
            heapq.heappush(max_heap, (-num, right))

            left = right - k + 1
            while max_heap[0][1] < left:
                heapq.heappop(max_heap)

            if left >= 0:
                window_maxima.append(-max_heap[0][0])

        return window_maxima
