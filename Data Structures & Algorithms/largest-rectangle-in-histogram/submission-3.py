class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        bar_count = len(heights)
        left_boundaries = [-1] * bar_count
        right_boundaries = [bar_count] * bar_count
        index_stack = []

        for index, current_height in enumerate(heights):
            while index_stack and heights[index_stack[-1]] > current_height:
                right_boundaries[index_stack.pop()] = index

            left_boundaries[index] = index_stack[-1] if index_stack else -1
            index_stack.append(index)

        max_area = 0

        for index, height in enumerate(heights):
            width = right_boundaries[index] - left_boundaries[index] - 1
            max_area = max(max_area, height * width)

        return max_area
