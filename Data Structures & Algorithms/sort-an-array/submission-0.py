class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(size: int, root: int):

            while True:

                largest = root
                left = 2 * root + 1
                right = 2 * root + 2

                if left < size and nums[left] > nums[largest]:
                    largest = left

                if right < size and nums[right] > nums[largest]:
                    largest = right
                
                if largest == root:
                    break
                
                nums[root], nums[largest] = nums[largest], nums[root]
                root = largest

        size = len(nums)

        for root in range(size // 2 - 1, -1, -1):
            heapify(size, root)

        for end in range(size - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(end, 0)

        return nums
