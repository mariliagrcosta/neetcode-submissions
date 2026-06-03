class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        boundary_map = {}
        longest_sequence = 0

        for num in nums:
            if num in boundary_map:
                continue

            left_len = boundary_map.get(num - 1, 0)
            right_len = boundary_map.get(num + 1, 0)
            sequence_len = left_len + right_len + 1
            longest_sequence = max(longest_sequence, sequence_len)

            boundary_map[num] = sequence_len
            boundary_map[num - left_len] = sequence_len
            boundary_map[num + right_len] = sequence_len

        return longest_sequence
