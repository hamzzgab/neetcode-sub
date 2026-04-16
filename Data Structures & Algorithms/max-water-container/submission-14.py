class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        """
         0, 1, 2, 3, 4, 5, 6, 7
        [1, 7, 2, 5, 4, 7, 3, 6]
                  l  r
         
        1 < 6 : 1 * (7i - 0i) : 7  -> STORE MAX: l += 1
        7 > 6 : 6 * (7i - 1i) : 36 -> STORE MAX: r -= 1
        7 > 3 : 3 * (6i - 1i) : 15 -> MAX=36   : r -= 1
        7 = 7 : 7 * (5i - 1i) : 28 -> MAX=36   : l += 1, r -= 1
        2 < 4 : 2 * (4i - 2i) : 4  -> MAX=36   : l += 1
        5 > 4 : 4 * (4i - 3i) : 4  -> MAX=36   : break
        """

        area = -1
        while l < r:
            if heights[l] < heights[r]:
                area = max(area, heights[l] * (r - l))
                l += 1
            elif heights[l] > heights[r]:
                area = max(area, heights[r] * (r - l))
                r -= 1
            else:
                area = max(area, heights[l] * (r - l))
                l += 1
                r -= 1
        return area

