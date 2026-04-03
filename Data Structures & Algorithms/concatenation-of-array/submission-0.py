class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_size = 2 * len(nums)
        new_arr = [None] * new_size

        for i in range(new_size):
            new_arr[i] = nums[i % (new_size//2)]

        return new_arr