class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1, len_2 = len(word1), len(word2)
        _min = min(len_1, len_2)

        l = 0

        res = []
        while l < _min:
            res.append(word1[l])
            res.append(word2[l])
            l += 1

        res.append(word1[l:])
        res.append(word2[l:])

        return ''.join(res)
