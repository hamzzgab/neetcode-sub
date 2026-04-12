class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            long = 0
            temp = num
            while temp in nums:                
                temp -= 1
                long += 1
            res = max(long, res)
        return res