class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        num_set = set(nums)
        result = 0
        for num in num_set:
            length = 0
            if num + 1 in num_set:                
                continue
            while num - length in num_set:
                length += 1
            result = max(length, result)
        return result
