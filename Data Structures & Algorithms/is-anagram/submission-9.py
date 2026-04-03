from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        if len(s) != len(t):
            return False

        for s_val, t_val in zip(s, t):
            hash_s[s_val] += 1
            hash_t[t_val] += 1

        return hash_s == hash_t