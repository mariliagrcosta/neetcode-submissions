class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_by_distance = sorted(
            arr,
            key=lambda num: (abs(num - x), num)
        )
        closest_elements = sorted_by_distance[:k]

        return sorted(closest_elements)
