class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        queue = deque(nums)
        queue.rotate(k)
        nums[:] = list(queue)
