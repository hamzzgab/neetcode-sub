class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1, 2, 4, 6]
        => [1, 1, 1, 1]
        => [1, 1, 2, 8]
        => [48, 8, 6, 1]
        [48, 24, 12, 8]


        nums=[-1,0,1,2,3]
        [1, 1, 1, 1, 1]
        - [1, -1, 0, 0, 0]
        - [0, -6, 6, 3, 1]

        """
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