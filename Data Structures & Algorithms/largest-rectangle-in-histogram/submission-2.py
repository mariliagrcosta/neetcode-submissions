class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        index_stack = []

        for index in range(len(heights) + 1):
            current_height = heights[index] if index < len(heights) else 0

            while index_stack and heights[index_stack[-1]] > current_height:
                popped_index = index_stack.pop()
                popped_height = heights[popped_index]
                width = index - index_stack[-1] - 1 if index_stack else index

                max_area = max(max_area, popped_height * width)

            index_stack.append(index)

        return max_area
