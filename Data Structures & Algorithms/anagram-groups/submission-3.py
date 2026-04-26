from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for _str in strs:
            counts = [0] * 26
            for char in _str:
                counts[ord(char) - ord('a')] += 1                
            hash[tuple(counts)].append(_str)
        return list(hash.values())