class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = 0
        for num in hash_set:
            longest = 1
            if num + 1 not in hash_set:
                while num - longest in hash_set:
                    longest += 1
            res = max(longest, res)
        return res
