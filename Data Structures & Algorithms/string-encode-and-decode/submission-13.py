class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for _str in strs:
            output += f'{len(_str)}#{_str}'
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):            
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            output.append(s[i:j])
            i = j
        return output

"""

5 0
# 1
H 2 i 
e 3
l 4
l 5
o 6
5 7 
# 8
W 9
o
r
l
d
"""
