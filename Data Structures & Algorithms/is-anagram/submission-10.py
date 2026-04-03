class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}


        for val in s:
            hash_s[val] = 1 + hash_s.get(val, 0)

        for val in t:
            hash_t[val] = 1 + hash_t.get(val, 0)
        
        return hash_s == hash_t