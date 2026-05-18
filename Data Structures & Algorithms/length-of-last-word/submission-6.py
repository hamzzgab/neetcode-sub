class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s) - 1
        res = 0
        if len(s) == 1:
            return 1

        while l >= 0:
            if s[l].isalnum():                
                res += 1
            elif res > 0 and not s[l].isalnum():
                return res
            l -= 1
        return res