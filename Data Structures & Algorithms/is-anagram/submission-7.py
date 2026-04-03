from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)

        for val in set(s):
            s_hash[val] = s.count(val)

        for val in set(t):            
            t_hash[val] = t.count(val)

        print(s_hash, t_hash)
        return t_hash == s_hash
