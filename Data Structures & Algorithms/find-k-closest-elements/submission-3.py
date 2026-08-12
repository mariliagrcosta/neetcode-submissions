import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []

        for num in arr:
            distance = abs(num - x)
            heapq.heappush(max_heap, (-distance, -num))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return sorted(-num for _, num in max_heap)
