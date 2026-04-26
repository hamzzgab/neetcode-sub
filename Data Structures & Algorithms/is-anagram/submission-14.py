class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        if len(s) != len(t):
            return False

        for val in s:
            hash_s[val] = hash_s.get(val, 0) + 1

        for val in t:
            hash_t[val] = hash_t.get(val, 0) + 1

        return hash_s == hash_t
            