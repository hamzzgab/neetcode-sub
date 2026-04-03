class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0, 0, 0]

        for index in nums:
            bucket[index] += 1

        print(bucket)

        i = 0
        for val, freq in enumerate(bucket):
            for _ in range(freq):
                nums[i] = val
                i += 1