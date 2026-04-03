from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for str in strs:
            count_str = [0] * 26
            for s in str:                
                count_str[ord(s) - ord('a')] += 1
            hash[tuple(count_str)].append(str)
        
        return list(hash.values())