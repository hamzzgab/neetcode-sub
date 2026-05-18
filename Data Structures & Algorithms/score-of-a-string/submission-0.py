class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) == 2:
            a, b = s[0], s[1]
            print(ord(a) , ord(b))
            return abs(ord(b) - ord(a))
        
        _sum = 0
        for i in range(1, len(s)):                            
            _sum += abs(ord(s[i - 1]) - ord(s[i]))            
            print(s[i - 1], s[i], _sum)
        return _sum