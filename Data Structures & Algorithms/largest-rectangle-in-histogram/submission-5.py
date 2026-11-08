class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        bar_count = len(heights)
        left_boundaries = [-1] * bar_count
        right_boundaries = [bar_count] * bar_count

        # Precompute left boundary for each bar using jump pointers
        for index in range(1, bar_count):
            probe_index = index - 1

            while probe_index >= 0 and heights[probe_index] >= heights[index]:
                probe_index = left_boundaries[probe_index]

            left_boundaries[index] = probe_index

        # Precompute right boundary for each bar using jump pointers
        for index in range(bar_count - 2, -1, -1):
            probe_index = index + 1

            while probe_index < bar_count and heights[probe_index] >= heights[index]:
                probe_index = right_boundaries[probe_index]

            right_boundaries[index] = probe_index

        # Calculate maximum rectangle area
        max_area = 0

        for index, height in enumerate(heights):
            width = right_boundaries[index] - left_boundaries[index] - 1
            max_area = max(max_area, height * width)

        return max_area
