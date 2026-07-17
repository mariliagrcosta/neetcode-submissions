class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        trapped_water = 0

        for i, current_height in enumerate(height):
            while stack and current_height > height[stack[-1]]:
                bottom = stack.pop()

                if not stack:
                    break

                left = stack[-1]
                width = i - left - 1
                bounded_height = min(height[left], current_height) - height[bottom]

                trapped_water += width * bounded_height

            stack.append(i)

        return trapped_water
