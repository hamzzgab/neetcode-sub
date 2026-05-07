class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1, len_2 = len(word1), len(word2)
        _min = min(len_1, len_2)

        l, r  = 0, 0

        res = ""
        print(l, _min)
        while l < _min:
            print(word1[l], word2[l])
            res += f'{word1[l]}{word2[l]}'
            l += 1
        
        res += word1[l:]
        res += word2[l:]

        return res

