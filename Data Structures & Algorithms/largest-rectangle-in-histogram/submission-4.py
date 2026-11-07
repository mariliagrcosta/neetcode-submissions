class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        bar_count = len(heights)
        left_boundaries = [-1] * bar_count
        right_boundaries = [bar_count] * bar_count
        index_stack = []

        # Pass 1: Find left boundary for each bar (left-to-right)
        for index in range(bar_count):
            while index_stack and heights[index_stack[-1]] >= heights[index]:
                index_stack.pop()

            if index_stack:
                left_boundaries[index] = index_stack[-1]

            index_stack.append(index)

        index_stack.clear()

        # Pass 2: Find right boundary for each bar (right-to-left)
        for index in range(bar_count - 1, -1, -1):
            while index_stack and heights[index_stack[-1]] >= heights[index]:
                index_stack.pop()

            if index_stack:
                right_boundaries[index] = index_stack[-1]

            index_stack.append(index)

        # Calculate maximum rectangle area
        max_area = 0

        for index, height in enumerate(heights):
            width = right_boundaries[index] - left_boundaries[index] - 1
            max_area = max(max_area, height * width)

        return max_area
