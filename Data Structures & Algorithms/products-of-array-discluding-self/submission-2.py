class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _len = len(nums)
        post = [1] * (_len)
        prefix = 1
        for i in range(len(nums)):
            post[i] = prefix
            prefix *= nums[i]
        print(post)

        infi = [1] * (_len)
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            infi[i] = prev * post[i]
            prev *= nums[i]
        print(infi)

        return infi