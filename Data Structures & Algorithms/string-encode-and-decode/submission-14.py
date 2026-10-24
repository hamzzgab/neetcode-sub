class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for _str in strs:
            output += f'{len(_str)}#{_str}'
        return output

    def decode(self, s: str) -> List[str]:
        output = []    
        i = 0
        while i < len(s) - 1:
            j = i

            while s[j] != '#':
                j += 1
            
            _length = int(s[i:j])
            i = j + 1
            j = _length + i
            output.append(s[i:j])            
            i = j
        return output