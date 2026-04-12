class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        for val in s:
            hash_s[val] = hash_s.get(val, 0) + 1

        hash_t = {}
        for val in t:
            hash_t[val] = hash_t.get(val, 0) + 1

        return hash_t == hash_s
