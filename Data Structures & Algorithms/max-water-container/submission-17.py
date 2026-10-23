class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container = 0
        l, r = 0, len(heights) - 1

        while l < r:
            length, height = (r - l), 0
            if heights[l] < heights[r]:
                height = heights[l]                
                l += 1
            elif heights[l] > heights[r]:
                height = heights[r]
                r -= 1
            else:                
                height = heights[r]
                l += 1
                r -= 1
            water = length * height
            container = max(container, water)

        return container