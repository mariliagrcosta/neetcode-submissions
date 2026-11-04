class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        bar_stack = []

        for index, current_height in enumerate(heights):
            current_start = index

            while bar_stack and bar_stack[-1][1] > current_height:
                popped_start, popped_height = bar_stack.pop()
                max_area = max(
                    max_area,
                    popped_height * (index - popped_start)
                )
                current_start = popped_start

            bar_stack.append((current_start, current_height))

        for start, height in bar_stack:
            max_area = max(max_area, height * (len(heights) - start))

        return max_area
