class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = 0
        res = 0

        for r in range(len(s)):
            print(s[r], r, l, map, end=' ')
            if s[r] in map:
                print('updated:', l, end=' ')
                l = max(map[s[r]] + 1, l)
            map[s[r]] = r
            print('updated:', map, end='\n')
            res = max(r - l + 1, res)
        
        return res
