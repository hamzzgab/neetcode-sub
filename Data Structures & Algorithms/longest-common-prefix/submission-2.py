class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0 or strs[0] == "":
            return res
                
        sorted_str = sorted(strs) 
        start = sorted_str[0]
        for i, _str in enumerate(start):
            match = True
            for j in range(1, len(sorted_str)):
                if i >= len(sorted_str[j]) or sorted_str[j][i] != _str:
                    match = False
                    break
            if match:
                res += _str
            else:
                break
            

        return res