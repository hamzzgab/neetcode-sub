from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        hash_set = defaultdict(list)

        for _str in strs:
            char_count = [0] * 26            
            for char in _str:
                char_count[ord(char) - ord('a')] += 1
            hash_set[tuple(char_count)].append(_str)

        return list(hash_set.values())