class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1, 2, 4, 6]

        [1, 1, 2, 8]
        [48, 24, 6, 1]
        """

        res = [1] * len(nums)
        temp = 1
        for i in range(len(nums)):
            res[i] *= temp
            temp *= nums[i]

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= temp
            temp *= nums[i]

        return res

