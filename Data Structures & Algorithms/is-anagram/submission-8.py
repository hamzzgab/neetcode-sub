from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        for val in s:
            hash_s[val] += 1

        for val in t:
            hash_t[val] += 1

        return hash_s == hash_t