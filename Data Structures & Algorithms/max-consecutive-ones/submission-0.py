class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _max, res = 0, 0
        for num in nums:
            if num == 1:
                res += 1
            else:                                
                res = 0
            _max = max(_max, res)
            print(res, _max)
        return _max