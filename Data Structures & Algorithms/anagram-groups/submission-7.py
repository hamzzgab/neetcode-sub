from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for _str in strs:
            char_arr = [0] * 26
            for char in _str:
                char_arr[ord(char) - ord('a')] += 1
            
            result[tuple(char_arr)].append(_str)
        return list(result.values())