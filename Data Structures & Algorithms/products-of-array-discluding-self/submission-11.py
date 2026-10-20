class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _len = len(nums)
        result = [1] * _len
        infix = 1
        for i in range(_len):
            result[i] *= infix
            infix *= nums[i]

        prefix = 1
        for i in range(_len - 1, -1, -1):            
            result[i] *= prefix
            prefix *= nums[i]

        return result