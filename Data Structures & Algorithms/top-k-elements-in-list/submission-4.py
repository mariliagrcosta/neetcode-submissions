class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in frequency_map.items():
            buckets[freq].append(num)

        top_k = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
