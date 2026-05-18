class Solution:
    def scoreOfString(self, s: str) -> int:
        _sum = 0
        for i in range(1, len(s)):                            
            _sum += abs(ord(s[i - 1]) - ord(s[i]))
        return _sum