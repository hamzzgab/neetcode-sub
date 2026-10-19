class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s, hash_t = {}, {}

        if len(s) != len(t):
            return False

        for val in set(s):
            hash_s[val] = s.count(val)
            hash_t[val] = t.count(val)


        return hash_s == hash_t

        

