import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        min_heap = []
        for num, freq in frequency_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for _, num in min_heap]