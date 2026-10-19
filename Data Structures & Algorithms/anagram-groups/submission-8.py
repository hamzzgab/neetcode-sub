from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        for _str in strs:
            count = [0] * 26
            for _char in _str:                
                count[ord(_char) - ord('a')] += 1
            
            hash_table[tuple(count)].append(_str)        
        return list(hash_table.values())