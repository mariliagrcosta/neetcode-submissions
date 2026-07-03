class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        count = 0
        start_index = 0

        while count < n:
            current_index = start_index
            carried_value = nums[start_index]

            while True:
                next_index = (current_index + k) % n
                nums[next_index], carried_value = carried_value, nums[next_index]
                current_index = next_index
                
                count += 1

                if start_index == current_index:
                    break

            start_index += 1
        