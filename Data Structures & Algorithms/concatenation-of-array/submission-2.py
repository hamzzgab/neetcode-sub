class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_size = len(nums) * 2
        new_arr = nums + ([-1] * len(nums))

        for i in range(len(nums), len(nums) * 2):            
            new_arr[i] = new_arr[i % len(nums)]

        return new_arr