class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for _str in strs:
            res += f"{len(_str)}#{_str}"
        return res

    def decode(self, s: str) -> List[str]:
        count = 10
        res = []
        i, j = 0, 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length

            res.append(s[i:j])
            i = j
        return res
