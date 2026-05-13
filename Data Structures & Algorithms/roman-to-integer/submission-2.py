class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        if len(s) == 1:
            return hash[s[0]]

        res = 0
        for i in range(len(s) - 1):
            mult = 1
            if (s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X')) or (s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C')) or (s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M')):
                mult = -1

            res += mult * hash[s[i]]
            print(s[i], hash[s[i]], res)
        
        return res + hash[s[i + 1]]