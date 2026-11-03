class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        bar_stack = []

        for index in range(len(heights) + 1):
            current_height = heights[index] if index < len(heights) else 0
            start = index

            while bar_stack and bar_stack[-1][1] > current_height:
                start, popped_height = bar_stack.pop()
                max_area = max(max_area, popped_height * (index - start))

            bar_stack.append((start, current_height))

        return max_area
