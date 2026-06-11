class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1, 2, 4, 6
        
        1, 1, 2, 8
        48 24 6  1

        48, 24, 12, 8
        """

        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

        infix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= infix
            infix *= nums[i]

        return result
