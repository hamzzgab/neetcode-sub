from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for _str in strs:
            count = [0] * 26
            for char in _str:
                count[ord(char) - ord('a')] += 1
            group[tuple(count)].append(_str)
        return list(group.values())