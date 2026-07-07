class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        queue = deque(nums)

        for _ in range(k):
            moved_element = queue.pop()
            queue.appendleft(moved_element)

        nums[:] = list(queue)
        