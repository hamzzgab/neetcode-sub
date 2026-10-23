class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container = 0
        l, r = 0, len(heights) - 1

        while l < r:
            length = (r - l)
            if heights[l] < heights[r]:
                water = length * heights[l]
                l += 1
            elif heights[l] > heights[r]:
                water = length * heights[r]
                r -= 1
            else:
                water = length * heights[r]
                l += 1
                r -= 1
            container = max(container, water)

        return container