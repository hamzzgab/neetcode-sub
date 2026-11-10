class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        sub_strings = set()        

        for r in range(len(s)):
            while s[r] in sub_strings:
                sub_strings.remove(s[l])
                l += 1
            sub_strings.add(s[r])
            res = max(res, len(sub_strings))
        return res