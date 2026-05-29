class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        sorted_items = dict(
            sorted(
                frequency_map.items(), 
                key=lambda item: item[1], 
                reverse=True
            )
        )
        
        unique_numbers = list(sorted_items)

        return unique_numbers[:k]
