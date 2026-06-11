from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for _str in strs:
            count = [0] * 26
            for char in _str:
                count[ord('a') - ord(char)] += 1

            result[tuple(count)].append(_str)

        return list(result.values())
            