class Solution:
    def __init__(self):
        self.len_str = []

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str in strs:
            res += str
            self.len_str.append(len(str))
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        for length in self.len_str:
            res.append(s[i:length + i])
            i += length
        
        return res
            
