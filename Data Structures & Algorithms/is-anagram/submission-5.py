from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)

        res = set(s) if len(set(s)) > len(set(t)) else set(t)

        for val in res:
            s_hash[val] = s.count(val)
            t_hash[val] = t.count(val)
            
        return t_hash == s_hash
