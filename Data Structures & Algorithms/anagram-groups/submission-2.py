from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect = defaultdict(list)
        for _str in strs:
            store = [0] * 26
            for char in _str:
                store[ord(char) - ord('a')] += 1
            collect[tuple(store)].append(_str)
        return list(collect.values())